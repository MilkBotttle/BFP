from . import validators
from django.forms.fields import CharField
from .ipv6cidr import clean_ipv6_cidr

class GenericIPNetworkField(CharField):
    def __init__(self, *, protocol='both', **kwargs):
        self.default_validators = validators.ip_network_validators(protocol)[0]
        super().__init__(**kwargs)

    def to_python(self, value):
        if value in self.empty_values:
            return ''
        value = value.strip()
        print("value:",value)
        if value and ':' in value:
            return clean_ipv6_cidr(value)
        return value
