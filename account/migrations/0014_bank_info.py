# Generated by Django 4.0.4 on 2022-05-31 19:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0013_rename_currency_code_currency_code_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Bank_Info",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("account_number", models.CharField(max_length=50)),
                ("account_name", models.CharField(max_length=100)),
                ("bank_name", models.CharField(max_length=100)),
                (
                    "currency",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account.currency",
                    ),
                ),
            ],
            options={
                "verbose_name": "Bank Info",
                "verbose_name_plural": "Bank Info",
            },
        ),
    ]
