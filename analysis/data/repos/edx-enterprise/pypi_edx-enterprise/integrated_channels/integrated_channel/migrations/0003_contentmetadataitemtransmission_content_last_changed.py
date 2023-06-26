# Generated by Django 2.2.24 on 2021-08-03 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrated_channel', '0002_learnerdatatransmissionaudit_subsection_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentmetadataitemtransmission',
            name='content_last_changed',
            field=models.DateTimeField(blank=True, help_text='Date of the last time the enterprise catalog associated with this metadata item was updated', null=True),
        ),
    ]
