# Generated by Django 4.0.3 on 2022-05-09 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_password2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='password2',
            field=models.CharField(max_length=300),
        ),
    ]
