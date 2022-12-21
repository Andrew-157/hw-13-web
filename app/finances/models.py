from django.db import models


class Income(models.Model):
    value = models.FloatField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.value


class OutcomeCategory(models.Model):
    name = models.CharField(max_length=56)


class Outcome(models.Model):
    category = models.ForeignKey(OutcomeCategory, on_delete=models.CASCADE)
    value = models.FloatField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.value
