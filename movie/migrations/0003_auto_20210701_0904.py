# Generated by Django 3.2.4 on 2021-07-01 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20210701_0841'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filmmodel',
            options={'ordering': ['pk'], 'verbose_name': 'film', 'verbose_name_plural': 'films'},
        ),
        migrations.AlterModelOptions(
            name='filmseriesmodel',
            options={'verbose_name': 'SERIES', 'verbose_name_plural': 'TV_SERIES'},
        ),
        migrations.AlterModelOptions(
            name='filmseriesseasonmodel',
            options={'verbose_name': 'Series_Season', 'verbose_name_plural': 'Series_Seasons'},
        ),
        migrations.AlterModelOptions(
            name='filmseriesvideomodel',
            options={'verbose_name': 'Season_series', 'verbose_name_plural': 'Season_TV_series'},
        ),
        migrations.RenameField(
            model_name='filmseriesvideomodel',
            old_name='count',
            new_name='series_number',
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='title',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='title_en',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='title_ru',
            field=models.CharField(max_length=15, null=True),
        ),
    ]