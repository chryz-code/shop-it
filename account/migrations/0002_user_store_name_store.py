# Generated by Django 4.0.3 on 2022-05-22 22:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="store_name",
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.CreateModel(
            name="Store",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("store_name", models.CharField(max_length=150, unique=True)),
                ("slugified_store_name", models.SlugField(max_length=255, unique=True)),
                ("store_description", models.TextField(blank=True, max_length=500)),
                (
                    "store_image",
                    models.ImageField(
                        default="store-images/default.jpg", upload_to="store-images/"
                    ),
                ),
                (
                    "customers",
                    models.ManyToManyField(
                        blank=True,
                        related_name="store_customers",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="store_owner",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "staffs",
                    models.ManyToManyField(
                        blank=True,
                        related_name="store_staffs",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Store",
                "verbose_name_plural": "Stores",
            },
        ),
    ]
