# Generated by Django 2.0.3 on 2018-04-01 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudvehicles', '0004_auto_20180401_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='mileage',
            field=models.BigIntegerField(default=0),
        ),
    ]
