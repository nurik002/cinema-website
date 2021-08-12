# Generated by Django 3.2.4 on 2021-07-01 03:41

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('title_en', models.CharField(max_length=10, null=True)),
                ('title_ru', models.CharField(max_length=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='QualityModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'quality',
                'verbose_name_plural': 'qualities',
            },
        ),
        migrations.AlterField(
            model_name='filmmodel',
            name='country',
            field=models.CharField(max_length=160, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='filmmodel',
            name='country_en',
            field=models.CharField(max_length=160, null=True, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='filmmodel',
            name='country_ru',
            field=models.CharField(max_length=160, null=True, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='filmmodel',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='filmmodel',
            name='description_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='filmmodel',
            name='description_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='filmmodel',
            name='release_year',
            field=models.IntegerField(default=0, verbose_name='release_year'),
        ),
        migrations.AlterField(
            model_name='filmmodel',
            name='running_time',
            field=models.IntegerField(verbose_name='running_time'),
        ),
        migrations.AlterField(
            model_name='filmseriesmodel',
            name='country',
            field=models.CharField(max_length=160, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='filmseriesmodel',
            name='country_en',
            field=models.CharField(max_length=160, null=True, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='filmseriesmodel',
            name='country_ru',
            field=models.CharField(max_length=160, null=True, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='filmseriesmodel',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='filmseriesmodel',
            name='description_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='filmseriesmodel',
            name='description_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='filmseriesmodel',
            name='release_year',
            field=models.IntegerField(default=0, verbose_name='release_year'),
        ),
        migrations.AlterField(
            model_name='filmseriesmodel',
            name='running_time',
            field=models.IntegerField(verbose_name='running_time'),
        ),
        migrations.AlterField(
            model_name='filmmodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='film', to='movie.categorymodel', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='filmmodel',
            name='quality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='film', to='movie.qualitymodel', verbose_name='quality'),
        ),
        migrations.AlterField(
            model_name='filmseriesmodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='series', to='movie.categorymodel', verbose_name='category'),
        ),
        migrations.AlterField(
            model_name='filmseriesmodel',
            name='quality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='series', to='movie.qualitymodel', verbose_name='quality'),
        ),
    ]