# Generated by Django 4.0.3 on 2022-05-09 05:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_delete_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='customers',
            field=models.ManyToManyField(blank=True, related_name='store_customers', to=settings.AUTH_USER_MODEL),
        ),
    ]
