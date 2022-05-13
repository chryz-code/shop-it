# Generated by Django 4.0.3 on 2022-05-13 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_address_default'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_line2',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Address Line 2'),
        ),
        migrations.AlterField(
            model_name='address',
            name='delivery_instructions',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Delivery Instructions'),
        ),
        migrations.AlterField(
            model_name='address',
            name='postcode',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Postcode'),
        ),
    ]
