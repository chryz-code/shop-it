# Generated by Django 4.0.3 on 2022-05-11 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_user_store_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='store_name',
            field=models.CharField(blank=True, max_length=150, unique=True),
        ),
    ]
