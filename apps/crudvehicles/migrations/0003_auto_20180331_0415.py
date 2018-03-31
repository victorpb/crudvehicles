# Generated by Django 2.0.3 on 2018-03-31 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crudvehicles', '0002_vehiclemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='vehiclemodel',
            name='name',
        ),
        migrations.AlterField(
            model_name='vehiclemodel',
            name='automaker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='auto_maker', to='crudvehicles.AutoMaker'),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vehicle_model', to='crudvehicles.VehicleModel'),
        ),
    ]