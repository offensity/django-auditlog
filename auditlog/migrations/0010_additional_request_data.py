import jsonfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auditlog", "0009_timestamp_id_index"),
    ]

    operations = [
        migrations.AddField(
            model_name="logentry",
            name="additional_request_data",
            field=jsonfield.fields.JSONField(null=True, blank=True),
        )
    ]
