# Generated by Django 4.1 on 2022-08-15 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0013_store_newsletter_newsletter"),
    ]

    operations = [
        migrations.RenameField(
            model_name="store_newsletter",
            old_name="customer",
            new_name="customers",
        ),
    ]
