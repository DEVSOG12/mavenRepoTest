# Generated by Django 2.2.20 on 2021-05-03 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise', '0129_enterprisecatalogquery_uuid_unique'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterprisecustomer',
            name='enable_integrated_customer_learner_portal_search',
            field=models.BooleanField(default=True, help_text='Checked by default. When unchecked, learners in organizations with an integrated channel (LMS) will not see the "Find a Course" option in the enterprise learner portal.', verbose_name='Enable learner portal search for LMS customers'),
        ),
        migrations.AlterField(
            model_name='historicalenterprisecustomer',
            name='enable_integrated_customer_learner_portal_search',
            field=models.BooleanField(default=True, help_text='Checked by default. When unchecked, learners in organizations with an integrated channel (LMS) will not see the "Find a Course" option in the enterprise learner portal.', verbose_name='Enable learner portal search for LMS customers'),
        ),
    ]
