# Generated by Django 3.2.15 on 2023-01-03 14:57

from django.db import connection, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xapi', '0010_auto_20221021_0159'),
    ]

    db_engine = connection.settings_dict['ENGINE']
    if 'sqlite3' in db_engine:
        operations = [
            migrations.AlterIndexTogether(
                name='xapilearnerdatatransmissionaudit',
                index_together={('enterprise_customer_uuid', 'plugin_configuration_id')},
            ),
        ]
    else:
        operations = [
            migrations.SeparateDatabaseAndState(
                state_operations=[
                    migrations.AlterIndexTogether(
                        name='xapilearnerdatatransmissionaudit',
                        index_together={('enterprise_customer_uuid', 'plugin_configuration_id')},
                    ),
                ],
                database_operations=[
                    migrations.RunSQL(sql="""
                        CREATE INDEX xapi_xldta_85936b55_idx
                        ON xapi_xapilearnerdatatransmissionaudit (enterprise_customer_uuid, plugin_configuration_id)
                        ALGORITHM=INPLACE LOCK=NONE
                    """, reverse_sql="""
                        DROP INDEX xapi_xldta_85936b55_idx
                        ON xapi_xapilearnerdatatransmissionaudit
                    """),
                ]
            ),
        ]