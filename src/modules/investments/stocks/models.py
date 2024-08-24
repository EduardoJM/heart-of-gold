from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

class Ticket(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name=_('user'),
        on_delete=models.CASCADE,
        related_name='tickets',
    )
    ticket = models.CharField(_('ticket'), max_length=10)

    def __str__(self):
        return self.ticket

    class Meta:
        verbose_name = _('ticket')
        verbose_name_plural = _('tickets')

class Tax(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name=_('user'),
        on_delete=models.CASCADE,
        related_name='taxes',
    )
    name = models.CharField(_('name'), max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('tax')
        verbose_name_plural = _('taxes')

class Invoice(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name=_('user'),
        on_delete=models.CASCADE,
        related_name='invoices',
    )
    number = models.CharField(_('note number'), max_length=100)
    net_value = models.IntegerField(_('net value'))

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = _('invoice')
        verbose_name_plural = _('invoices')

class InvoiceTax(models.Model):
    invoice = models.ForeignKey(
        Invoice,
        verbose_name=_('invoice'),
        on_delete=models.CASCADE,
        related_name='taxes',
    )
    tax = models.ForeignKey(
        Tax,
        verbose_name=_('tax'),
        on_delete=models.CASCADE,
        related_name='invoice_taxes',
    )
    value = models.IntegerField(_('value'))

    def __str__(self):
        return f"{str(self.tax)}: {self.value}"

    class Meta:
        verbose_name = _('invoice tax')
        verbose_name_plural = _('invoice taxes')

class Stock(models.Model):
    TYPE_BUY = 'BUY'
    TYPE_SALE = 'SALE'
    TYPES = ((TYPE_BUY, _('buy')), (TYPE_SALE, _('sale')))

    user = models.ForeignKey(
        User,
        verbose_name=_('user'),
        on_delete=models.CASCADE,
        related_name='stocks',
    )
    invoice = models.ForeignKey(
        Invoice,
        verbose_name=_('invoice'),
        on_delete=models.CASCADE,
        related_name='stocks',
    )
    ticket = models.ForeignKey(
        Ticket,
        verbose_name=_('ticket'),
        on_delete=models.CASCADE,
        related_name='stocks',
    )
    stock_type = models.CharField(_('stock type'), max_length=10, choices=TYPES)
    specification = models.CharField(_('specification'), max_length=100, blank=True, default='')
    is_fractioned = models.BooleanField(_('is fractioned'))
    quantity = models.IntegerField(_('quantity'))
    unit_price = models.IntegerField(_('unit price'))
    price = models.IntegerField(_('price'))
    notes = models.TextField(_('notes'), blank=True, default='')

    def __str__(self):
        return str(self.ticket)

    class Meta:
        verbose_name = _('stock')
        verbose_name_plural = _('stocks')
