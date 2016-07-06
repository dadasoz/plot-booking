# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 04:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import plots.lib.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('booking_api', '0001_initial'),
        ('customer_api', '0004_auto_20160703_0530'),
        ('projects_api', '0013_project_village'),
    ]

    operations = [
        migrations.CreateModel(
            name='EMI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('updated_at', plots.lib.utils.AutoDateTimeField(default=django.utils.timezone.now)),
                ('emi_schedule_date', models.DateField(null=True)),
                ('amount', models.DecimalField(decimal_places=10, max_digits=19)),
                ('paid', models.BooleanField(default=False)),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emi_sale', to='customer_api.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_emi_enabled', models.CharField(blank=True, max_length=254)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('updated_at', plots.lib.utils.AutoDateTimeField(default=django.utils.timezone.now)),
                ('sale_completed', models.BooleanField(default=False)),
                ('basic_cost', models.DecimalField(decimal_places=10, max_digits=19)),
                ('sales_cost', models.DecimalField(decimal_places=10, max_digits=19)),
                ('remaning_cost', models.DecimalField(decimal_places=10, max_digits=19)),
                ('booking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sale_booking', to='booking_api.Booking')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_customer', to='customer_api.Customer')),
                ('plot_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_plots', to='projects_api.Plots')),
            ],
        ),
        migrations.CreateModel(
            name='SaleTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=10, max_digits=19)),
                ('trasaction_type', models.CharField(blank=True, max_length=254)),
                ('trasaction_type_no', models.CharField(blank=True, max_length=254)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('is_emi', models.BooleanField(default=False)),
                ('status', models.BooleanField(default=True)),
                ('emi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_transaction_emi', to='accounts_api.EMI')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_transaction_sale', to='customer_api.Customer')),
            ],
        ),
    ]
