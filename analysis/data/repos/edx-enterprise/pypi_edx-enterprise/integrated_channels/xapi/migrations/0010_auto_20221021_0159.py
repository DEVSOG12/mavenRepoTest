# Generated by Django 3.2.16 on 2022-10-21 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xapi', '0009_xapilearnerdatatransmissionaudit_api_record'),
    ]

    operations = [
        migrations.AddField(
            model_name='xapilearnerdatatransmissionaudit',
            name='content_title',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='xapilearnerdatatransmissionaudit',
            name='progress_status',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='xapilearnerdatatransmissionaudit',
            name='user_email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
