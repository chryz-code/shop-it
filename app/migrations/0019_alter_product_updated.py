# Generated by Django 4.1 on 2022-08-16 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0018_alter_newsletter_updated"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
