# Generated by Django 3.2.4 on 2021-08-03 13:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movie', '0016_alter_filmseriesvideomodel_created_at'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FilmCommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('liked', models.IntegerField(default=0, verbose_name='liked')),
                ('unliked', models.IntegerField(default=0, verbose_name='unliked')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='film_comments', to='movie.filmmodel', verbose_name='film')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='film_comments_user', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'film_comment',
                'verbose_name_plural': 'films_comments',
            },
        ),
        migrations.CreateModel(
            name='SeriesCommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('liked', models.IntegerField(default=0, verbose_name='liked')),
                ('unliked', models.IntegerField(default=0, verbose_name='unliked')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='series_comments', to='movie.filmseriesmodel', verbose_name='series')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='series', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'series_comment',
                'verbose_name_plural': 'series_comments',
            },
        ),
        migrations.CreateModel(
            name='ReviewModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='title')),
                ('review', models.TextField(blank=True, null=True, verbose_name='review')),
                ('rating', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='rating')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='movie.filmmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'review',
                'verbose_name_plural': 'reviews',
            },
        ),
        migrations.CreateModel(
            name='LikeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_like', models.IntegerField(default=0, verbose_name='type_like')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_comments', to='review.filmcommentmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like_user', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'like',
                'verbose_name_plural': 'likes',
            },
        ),
    ]
