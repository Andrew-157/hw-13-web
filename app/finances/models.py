from django.db import models


class Income(models.Model):
    value = models.FloatField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.value


class Category(models.Model):
    name = models.CharField()


class Outcome(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    value = models.FloatField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.value
