# Generated by Django 2.2.24 on 2021-10-05 10:52

import jsonfield.fields

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('integrated_channel', '0004_contentmetadataitemtransmission_enterprise_customer_catalog_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentmetadataitemtransmission',
            name='channel_metadata',
            field=jsonfield.fields.JSONField(),
        ),
    ]
