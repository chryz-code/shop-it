# Generated by Django 3.2.4 on 2022-03-02 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20220302_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_2',
            field=models.ImageField(upload_to='product-images/'),
        ),
    ]
