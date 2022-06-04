# Generated by Django 4.0.4 on 2022-06-04 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0002_shipping_method'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=300)),
                ('password2', models.CharField(max_length=300)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='account.store')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('postcode', models.CharField(blank=True, max_length=50, null=True, verbose_name='Postcode')),
                ('address_line', models.CharField(max_length=255, verbose_name='Address Line 1')),
                ('address_line2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address Line 2')),
                ('delivery_instructions', models.CharField(blank=True, max_length=255, null=True, verbose_name='Delivery Instructions')),
                ('country', models.CharField(max_length=200, verbose_name='Country')),
                ('state', models.CharField(max_length=200, verbose_name='State')),
                ('city', models.CharField(max_length=200, verbose_name='City')),
                ('default', models.BooleanField(default=False, verbose_name='Default')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer', verbose_name='Customer')),
            ],
        ),
    ]
