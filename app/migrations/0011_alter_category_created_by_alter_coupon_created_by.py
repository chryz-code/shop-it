# Generated by Django 4.0.4 on 2022-05-27 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_alter_store_store_image'),
        ('app', '0010_alter_category_created_by_alter_coupon_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.store'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.store'),
        ),
    ]
