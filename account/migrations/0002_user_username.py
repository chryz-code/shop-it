# Generated by Django 4.0.3 on 2022-03-03 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='CODE', max_length=200, unique=True),
        ),
    ]
