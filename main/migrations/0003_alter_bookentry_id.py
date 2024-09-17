# Generated by Django 5.1 on 2024-09-17 04:26

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_bookentry_delete_product"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookentry",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]
