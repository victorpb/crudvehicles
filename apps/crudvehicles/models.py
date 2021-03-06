from django.db import models
from dj.choices.fields import ChoiceField
from .choices import ModelsTypesChoices


class AutoMaker(models.Model):
    name = models.CharField(max_length=100, blank=False,
                            null=False, unique=True)

    def __str__(self):
        return self.name


class VehicleModel(models.Model):

    name = models.CharField(
        max_length=100,
        blank=False,
        null=False)

    model = ChoiceField(
        choices=ModelsTypesChoices,
        default=ModelsTypesChoices.car)

    engine = models.FloatField(
        null=False,
        blank=False)

    automaker = models.ForeignKey(
        AutoMaker,
        related_name='auto_maker',
        on_delete=models.PROTECT)

    def __str__(self):
        return 'AutoMaker {} - engine {} - model - {}'.format(
            self.automaker.name, self.engine, self.model)


class Vehicle(models.Model):

    color = models.CharField(
        max_length=30,
        blank=False,
        null=False)

    mileage = models.BigIntegerField(
        null=False,
        blank=False,
        default=0)

    model = models.ForeignKey(
        VehicleModel,
        related_name='vehicle_model',
        on_delete=models.PROTECT)

    def __str__(self):
        return 'Model {} -  Color {}'.format(self.model.name, self.color)
