# Generated by Django 3.2.5 on 2023-05-30 19:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='DDL',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
