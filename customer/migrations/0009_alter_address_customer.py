# Generated by Django 4.0.4 on 2022-06-03 20:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0008_remove_address_full_name_remove_address_phone_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="customer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="customer.customer",
                verbose_name="Customer",
            ),
        ),
    ]
