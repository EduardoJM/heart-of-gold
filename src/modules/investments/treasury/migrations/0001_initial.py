# Generated by Django 5.0 on 2024-08-25 17:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TreasuryBondInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='name')),
                ('description', models.TextField(blank=True, default='', verbose_name='description')),
                ('unit_price', models.DecimalField(decimal_places=6, max_digits=15, verbose_name='unit price')),
            ],
        ),
        migrations.CreateModel(
            name='TreasuryBond',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('units', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='units')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to=settings.AUTH_USER_MODEL, verbose_name='user')),
                ('bond_information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bonds', to='treasury.treasurybondinformation', verbose_name='bond information')),
            ],
        ),
    ]
