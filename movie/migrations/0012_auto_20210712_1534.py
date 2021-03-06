# Generated by Django 3.2.4 on 2021-07-12 10:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0011_auto_20210711_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmcommentmodel',
            name='film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='film_comments', to='movie.filmmodel', verbose_name='film'),
        ),
        migrations.AlterField(
            model_name='filmseriesvideomodel',
            name='created_at',
            field=models.DateField(default=datetime.date(2021, 7, 12), verbose_name='created_at'),
        ),
        migrations.AlterField(
            model_name='seriescommentmodel',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='series_comments', to='movie.filmseriesmodel', verbose_name='series'),
        ),
    ]
