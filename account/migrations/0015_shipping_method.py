# Generated by Django 4.0.4 on 2022-06-01 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_bank_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping_Method',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=250)),
                ('price', models.PositiveIntegerField(default=0)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipping_method', to='account.store')),
            ],
        ),
    ]
