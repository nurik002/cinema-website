# Generated by Django 3.2.4 on 2021-07-13 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0013_auto_20210713_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likemodel',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='likemodel',
            name='user',
        ),
        migrations.RemoveField(
            model_name='reviewmodel',
            name='film',
        ),
        migrations.RemoveField(
            model_name='seriescommentmodel',
            name='liked',
        ),
        migrations.RemoveField(
            model_name='seriescommentmodel',
            name='series',
        ),
        migrations.RemoveField(
            model_name='seriescommentmodel',
            name='user',
        ),
        migrations.DeleteModel(
            name='FilmCommentModel',
        ),
        migrations.DeleteModel(
            name='LikeModel',
        ),
        migrations.DeleteModel(
            name='ReviewModel',
        ),
        migrations.DeleteModel(
            name='SeriesCommentModel',
        ),
    ]
