# Generated by Django 4.0.4 on 2022-06-09 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0006_payment_order"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="payment",
            name="currency",
        ),
    ]
