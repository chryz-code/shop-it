# Generated by Django 4.0.6 on 2022-08-04 22:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_wallet_transanction'),
    ]

    operations = [
        migrations.AddField(
            model_name='wallet_transanction',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
