from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

class TreasuryBondInformation(models.Model):
    name = models.CharField(
        _('name'),
        max_length=100,
        unique=True,
    )
    description = models.TextField(_('description'), blank=True, default='')
    unit_price = models.DecimalField(_('unit price'), max_digits=15, decimal_places=6)

    # TODO: add more fields from:
    # https://www.tesourodireto.com.br/json/br/com/b3/tesourodireto/service/api/treasurybondsinfo.json

    def __str__(self):
        return self.name

class TreasuryBond(models.Model):
    bond_information = models.ForeignKey(
        TreasuryBondInformation,
        verbose_name=_('bond information'),
        on_delete=models.CASCADE,
        related_name='bonds',
    )
    user = models.ForeignKey(
        User,
        verbose_name=_('user'),
        on_delete=models.CASCADE,
        related_name='tickets',
    )
    units = models.DecimalField(
        _('units'),
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return str(self.bond)
