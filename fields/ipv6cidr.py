import ipaddress
from django.utils.translation import gettext_lazy as _, ngettext_lazy
from django.core.exceptions import ValidationError

def clean_ipv6_cidr(ip_str, error_message=_("This is not a valid IPv6 network.")):
    """
    Clean an IPv6 network string.
    Raise ValidationError if the address is invalid.
    Replace the longest continuous zero-sequence with "::", remove leading
    zeroes, and make sure all hextets are lowercase.
    Args:
        ip_str: A valid IPv6 network.
        error_message: An error message used in the ValidationError.
    Return a compressed IPv6 network or the same value.
    """
    try:
        print(ip_str)
        addr = ipaddress.IPv6Network(ip_str)
    except ValueError:
        raise ValidationError(error_message, code='invalid')

    return str(addr)


