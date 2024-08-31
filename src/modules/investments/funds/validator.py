from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError
from .registry import registry

def validate_fund_name(value: str):
    names = registry.get_names()
    if value not in names:
        raise ValidationError(_('unsupported fund name.'))
