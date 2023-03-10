# Generated by Django 4.1.4 on 2022-12-24 06:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0007_alter_income_pub_date_alter_outcome_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='pub_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='outcome',
            name='pub_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
    ]
