# Generated by Django 4.1 on 2022-08-25 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0026_shipping_company"),
    ]

    operations = [
        migrations.AddField(
            model_name="shipping_method",
            name="shipping_company",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.shipping_company",
            ),
        ),
    ]
