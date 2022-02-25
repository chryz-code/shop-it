# Generated by Django 4.0.2 on 2022-02-21 23:03

import django.contrib.auth.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="slugified_username",
            new_name="slugified_store_name",
        ),
        migrations.AddField(
            model_name="user",
            name="store_name",
            field=models.CharField(
                default=django.utils.timezone.now, max_length=150, unique=True
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(
                error_messages={"unique": "A user with that username already exists."},
                help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                max_length=150,
                unique=True,
                validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                verbose_name="username",
            ),
        ),
    ]
