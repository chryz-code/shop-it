# Generated by Django 4.0.3 on 2022-03-03 16:37

import ckeditor.fields
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(db_index=True, max_length=255)),
                ("slug", models.SlugField(max_length=255, unique=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="category_creator",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="ProductUnit",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("image_1", models.ImageField(upload_to="product-images/")),
                ("image_2", models.ImageField(upload_to="product-images/")),
                (
                    "image_3",
                    models.ImageField(
                        blank=True, null=True, upload_to="product-images/"
                    ),
                ),
                (
                    "image_4",
                    models.ImageField(
                        blank=True, null=True, upload_to="product-images/"
                    ),
                ),
                ("slug", models.SlugField(max_length=255, unique=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=6)),
                ("in_stock", models.BooleanField(default=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now_add=True)),
                ("availability", models.IntegerField(default=1)),
                (
                    "product_details",
                    ckeditor.fields.RichTextField(
                        blank=True, max_length=300, null=True
                    ),
                ),
                (
                    "discount_percentage",
                    models.IntegerField(
                        blank=True,
                        default=0,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(100),
                        ],
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="category",
                        to="app.category",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_creator",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "product_unit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_unit",
                        to="app.productunit",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Products",
                "ordering": ("-created",),
            },
        ),
    ]
