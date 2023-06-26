# Generated by Django 3.2.15 on 2022-09-13 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrated_channel', '0016_contentmetadataitemtransmission_content_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentmetadataitemtransmission',
            name='friendly_status_message',
            field=models.CharField(blank=True, default=None, help_text='A user-friendly API response status message.', max_length=255, null=True),
        ),
    ]
