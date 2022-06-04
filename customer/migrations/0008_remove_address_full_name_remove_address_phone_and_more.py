# Generated by Django 4.0.4 on 2022-06-03 20:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("customer", "0007_alter_customer_store"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="address",
            name="full_name",
        ),
        migrations.RemoveField(
            model_name="address",
            name="phone",
        ),
        migrations.AlterField(
            model_name="address",
            name="customer",
            field=models.ForeignKey(
                default=26,
                on_delete=django.db.models.deletion.CASCADE,
                to="customer.customer",
                verbose_name="Customer",
            ),
        ),
    ]
