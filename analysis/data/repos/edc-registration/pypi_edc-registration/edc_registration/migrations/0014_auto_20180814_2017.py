# Generated by Django 2.1 on 2018-08-14 18:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("edc_registration", "0013_auto_20180813_1614")]

    operations = [
        migrations.AlterModelOptions(
            name="registeredsubject",
            options={
                "ordering": ["subject_identifier"],
                "permissions": (
                    ("display_firstname", "Can display first name"),
                    ("display_lastname", "Can display last name"),
                    ("display_dob", "Can display DOB"),
                    ("display_identity", "Can display identity number"),
                    ("display_initials", "Can display initials"),
                ),
                "verbose_name": "Registered Subject",
            },
        )
    ]
