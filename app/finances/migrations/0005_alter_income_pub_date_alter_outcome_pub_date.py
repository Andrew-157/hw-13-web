# Generated by Django 4.1.4 on 2022-12-22 07:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0004_alter_income_pub_date_alter_outcome_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 22, 7, 20, 8, 30015, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='outcome',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 22, 7, 20, 8, 70043, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
    ]
