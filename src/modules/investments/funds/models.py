from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from .validator import validate_fund_name

User = get_user_model()

class Fund(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name=_('user'),
        on_delete=models.CASCADE,
        related_name='funds',
    )
    name = models.CharField(
        _('name'),
        max_length=255,
        validators=[validate_fund_name]
    )
    buy_date = models.DateField(_('buy date'))
    buy_value = models.DecimalField(_('buy value'), max_digits=15, decimal_places=2)
    currently_value = models.DecimalField(_('currently value'), max_digits=15, decimal_places=2)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _('fund')
        verbose_name_plural = _('funds')
