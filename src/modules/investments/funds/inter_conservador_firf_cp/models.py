from typing import Optional
from datetime import date
from django.db import models
from django.utils.translation import gettext_lazy as _
from .integration import CumulativeReturnChartLineItem

class CumulativeReturnManager(models.Manager):
    def update_from_integration_axis(self, axis: CumulativeReturnChartLineItem):
        date_str = axis.xAxis
        month_str, day_str, year_str = date_str.split('/')
        year_str = f"20{year_str}"
        item_date = date(int(year_str), int(month_str), int(day_str))
        cumulated_return = float(axis.yAxis)
        return self.update_or_create(
            date=item_date,
            defaults={ 'cumulated_return': cumulated_return }
        )
    
    def find_nearest_up_date(self, date: date) -> Optional["CumulativeReturn"]:
        return self.filter(date__gte=date).first()

    def find_nearest_down_date(self, date: date) -> Optional["CumulativeReturn"]:
        return self.filter(date__lte=date).last()

class CumulativeReturn(models.Model):
    date = models.DateField(_('date'))
    cumulated_return = models.DecimalField(_('cumulated return'), max_digits=12, decimal_places=2)

    objects: CumulativeReturnManager = CumulativeReturnManager()

    class Meta:
        verbose_name = _('cumulative return')
        verbose_name_plural = _('cumulative returns')
