# Generated by Django 4.0.4 on 2022-06-01 13:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0015_shipping_method"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bank_info",
            name="currency",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="account.currency",
            ),
        ),
        migrations.AlterField(
            model_name="store",
            name="currency",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="currency",
                to="account.currency",
            ),
        ),
    ]
