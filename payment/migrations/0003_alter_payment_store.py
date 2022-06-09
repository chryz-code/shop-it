# Generated by Django 4.0.4 on 2022-06-07 12:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_alter_bank_info_currency_alter_store_currency"),
        ("payment", "0002_payment_store"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="store",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="account.store"
            ),
        ),
    ]
