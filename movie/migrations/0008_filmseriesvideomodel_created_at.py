# Generated by Django 3.2.4 on 2021-07-02 06:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_auto_20210701_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmseriesvideomodel',
            name='created_at',
            field=models.DateField(default=datetime.date(2021, 7, 2), verbose_name='created_at'),
        ),
    ]