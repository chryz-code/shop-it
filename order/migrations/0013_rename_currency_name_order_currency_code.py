# Generated by Django 4.0.4 on 2022-06-09 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0012_alter_order_currency_name_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="currency_name",
            new_name="currency_code",
        ),
    ]
