# Generated by Django 4.0.4 on 2022-06-07 15:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0005_remove_payment_order"),
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="payment",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="payment.payment",
            ),
        ),
    ]
