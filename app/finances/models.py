from django.db import models
from django.utils import timezone


class Income(models.Model):
    value = models.FloatField()
    pub_date = models.DateField(
        'date published', default=timezone.now().date())


class OutcomeCategory(models.Model):
    name = models.CharField(max_length=56)


class Outcome(models.Model):
    category = models.ForeignKey(OutcomeCategory, on_delete=models.CASCADE)
    value = models.FloatField()
    pub_date = models.DateField(
        'date published', default=timezone.now().date())
