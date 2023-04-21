from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auditlog", "0010_additional_request_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="logentry",
            name="action",
            field=models.PositiveSmallIntegerField(
                choices=[(0, "create"), (1, "update"), (2, "delete")],
                db_index=True,
                verbose_name="action",
            ),
        ),
    ]
