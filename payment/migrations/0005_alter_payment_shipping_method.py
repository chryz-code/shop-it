# Generated by Django 4.0.4 on 2022-06-04 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_alter_bank_info_currency_alter_store_currency'),
        ('payment', '0004_alter_payment_address_line_alter_payment_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='shipping_method',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='account.shipping_method'),
        ),
    ]
