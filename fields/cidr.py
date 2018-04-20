from django.db.models import Field
from . import forms
from . import validators
from .ipv6cidr import clean_ipv6_cidr 
from django.utils.translation import gettext_lazy as _, ngettext_lazy

class GenericIPNetworkField(Field):
    """
    Support CIDR input
     ipv4 0.0.0.0/0
     ipv6 ::::/0
    """
    empty_strings_allowed = False
    description = _("GenericIPNetworkField")
    default_error_messages = {}

    def __init__(self, verbose_name=None, name=None, protocol='both',
                 *args, **kwargs):
        self.protocol = protocol
        self.default_validators, invalid_error_message = \
            validators.ip_network_validators(protocol)
        self.default_error_messages['invalid'] = invalid_error_message
        kwargs['max_length'] = 43 # ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff/128
        super().__init__(verbose_name, name, *args, **kwargs)

    def check(self, **kwargs):
        errors = super().check(**kwargs)
        errors.extend(self._check_blank_and_null_values(**kwargs))
        return errors

    def _check_blank_and_null_values(self, **kwargs):
        if not getattr(self, 'null', False) and getattr(self, 'blank', False):
            return [
                checks.Error(
                    'GenericIPNetworkField cannot have blank=True if null=False, '
                    'as blank values are stored as nulls.',
                    obj=self,
                    id='fields.E150',
                )
            ]
        return []

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        if self.protocol != "both":
            kwargs['protocol'] = self.protocol
        if kwargs.get("max_length") == 43:
            del kwargs['max_length']
        return name, path, args, kwargs

    def get_internal_type(self):
        return "GenericIPNetworkField"

    def to_python(self, value):
        import ipdb;ipdb.set_trace()
        if value is None:
            return None
        if not isinstance(value, str):
            value = str(value)
        value = value.strip()
        if ':' in value:
            return clean_ipv6_network(value, self.unpack_ipv4, self.error_messages['invalid'])
        return value

    def get_db_prep_value(self, value, connection, prepared=False):
        if not prepared:
            value = self.get_prep_value(value)
        return connection.ops.adapt_ipaddressfield_value(value)

    def get_prep_value(self, value):
        value = super().get_prep_value(value)
        if value is None:
            return None
        if value and ':' in value:
            try:
                return clean_ipv6_cidr(value)
            except exceptions.ValidationError:
                pass
        return str(value)

    def formfield(self, **kwargs):
        defaults = {
            'protocol': self.protocol,
            'form_class': forms.GenericIPNetworkField,
        }
        defaults.update(kwargs)
        return super().formfield(**defaults)
