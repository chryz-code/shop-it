# Generated by Django 3.2.4 on 2022-02-23 13:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_auto_20220222_1517"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product_Order_Count",
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
                ("order_count", models.IntegerField(default=1)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_order_count",
                        to="app.product",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Product Order Count",
                "ordering": ("-order_count",),
            },
        ),
    ]
