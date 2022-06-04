# Generated by Django 4.0.4 on 2022-06-03 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("payment", "0003_payment_postcode"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="address_line",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="payment",
            name="city",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="payment",
            name="country",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="payment",
            name="state",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
