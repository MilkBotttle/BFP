import ipaddress
from django.utils.translation import gettext_lazy as _, ngettext_lazy
from django.core.exceptions import ValidationError

def validate_ipv4_network(value):
    try:
        ipaddress.IPv4Network(value)
    except ValueError:
        raise ValidationError(_('Enter a valid IPv4 network.'), code='invalid')

def validate_ipv6_network(value):
    try:
        ipaddress.IPv6Network(value)
    except ValueError:
        raise ValidationError(_('Enter a valid IPv6 network.'), code='invalid')

def validate_ipv46_network(value):
    try:
        validate_ipv4_network(value)
    except ValidationError:
        try:
            validate_ipv6_network(value)
        except ValidationError:
            raise ValidationError(_('Enter a valid IPv4 or IPv6 network.'), code='invalid')

ip_network_validator_map = {
    'both': ([validate_ipv46_network], _('Enter a valid IPv4 or IPv6 network.')),
    'ipv4': ([validate_ipv4_network], _('Enter a valid IPv4 network.')),
    'ipv6': ([validate_ipv6_network], _('Enter a valid IPv6 network.')),
}

def ip_network_validators(protocol):
    """
    Depending on the given parameters, return the appropriate validators for
    the GenericIPNetworkField.
    """
    try:
        return ip_network_validator_map[protocol.lower()]
    except KeyError:
        raise ValueError("The protocol '%s' is unknown. Supported: %s"
                         % (protocol, list(ip_network_validator_map)))
