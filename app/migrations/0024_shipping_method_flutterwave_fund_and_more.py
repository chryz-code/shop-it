# Generated by Django 4.1 on 2022-08-22 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0023_alter_shipping_method_location"),
    ]

    operations = [
        migrations.AddField(
            model_name="shipping_method",
            name="flutterwave_fund",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="shipping_method",
            name="shopit_fund",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="shipping_method",
            name="total_funds",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
