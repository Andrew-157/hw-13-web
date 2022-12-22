# Generated by Django 4.1.4 on 2022-12-22 15:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0005_alter_income_pub_date_alter_outcome_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 22, 15, 46, 21, 228655, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='outcome',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2022, 12, 22, 15, 46, 21, 272659, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
    ]
