# Generated by Django 2.2.14 on 2020-09-03 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0109_remove_use_enterprise_catalog_sample'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterprisecustomer',
            name='default_contract_discount',
            field=models.DecimalField(blank=True, decimal_places=5, help_text='Specifies the discount percent used for enrollments from the enrollment API where capturing the discount per order is not possible. This is passed to ecommerce when creating orders for financial data reporting.', max_digits=8, null=True),
        ),
        migrations.AddField(
            model_name='historicalenterprisecustomer',
            name='default_contract_discount',
            field=models.DecimalField(blank=True, decimal_places=5, help_text='Specifies the discount percent used for enrollments from the enrollment API where capturing the discount per order is not possible. This is passed to ecommerce when creating orders for financial data reporting.', max_digits=8, null=True),
        ),
    ]
