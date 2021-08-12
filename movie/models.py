import datetime

from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Sum, Q
from django.utils.translation import ugettext_lazy as _

UserModel = get_user_model()


class QualityModel(models.Model):
    title = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('quality')
        verbose_name_plural = _('qualities')


class CategoryModel(models.Model):
    title = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class GenreModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('genre')
        verbose_name_plural = _('genres')


# class PostManager(models.Manager):
#     def search(self, query=None):
#         qs = self.get_queryset()
#         if query is not None:
#             or_lookup = (Q(title__icontains=query))
#             qs = qs.filter(or_lookup).distinct()
#         return qs


class FilmAbstractModel(models.Model):
    cover = models.ImageField(upload_to='covers', verbose_name=_('cover'))
    title = models.CharField(max_length=250, verbose_name=_('title'), db_index=True)
    IMDb = models.FloatField(default=0)
    rating = models.FloatField(verbose_name=_('rating'), default=0)
    recommended_age = models.IntegerField(verbose_name=_('recommended_age'))
    release_year = models.IntegerField(default=0, verbose_name=_('release_year'))
    country = models.CharField(max_length=160, verbose_name=_('country'))
    description = RichTextField(verbose_name=_('description'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))


    class Meta:
        abstract = True


class FilmModel(FilmAbstractModel):
    film = models.FileField(upload_to='films', verbose_name=_('film'))
    running_time = models.IntegerField(verbose_name=_('running_time'))
    genre = models.ManyToManyField(
        GenreModel, related_name='films', verbose_name=_('genre')
    )
    quality = models.ForeignKey(
        QualityModel, on_delete=models.PROTECT, verbose_name=_('quality'), related_name='film'
    )
    category = models.ForeignKey(
        CategoryModel, on_delete=models.PROTECT, verbose_name=_('category'), related_name='film'
    )

    def get_rating(self):
        return self.reviews.aggregate(Sum('rating'))['rating__sum'] / self.reviews.count()

    def get_comments(self):
        return self.film_comments.order_by('-pk')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('film')
        verbose_name_plural = _('films')


class FilmSeriesModel(FilmAbstractModel):
    genre = models.ManyToManyField(
        GenreModel, related_name='film_series', verbose_name=_('genre')
    )
    quality = models.ForeignKey(
        QualityModel, on_delete=models.PROTECT, verbose_name=_('quality'), related_name='series'
    )
    category = models.ForeignKey(
        CategoryModel, on_delete=models.PROTECT, related_name='series', verbose_name=_('category')
    )

    def get_comments(self):
        return self.series_comments.order_by('-pk')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('SERIES')
        verbose_name_plural = _('TV_SERIES')


class FilmSeriesSeasonModel(models.Model):
    season = models.IntegerField(verbose_name=_('season'))
    series = models.ForeignKey(FilmSeriesModel, on_delete=models.CASCADE, related_name='season')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    class Meta:
        verbose_name = _('Series_Season')
        verbose_name_plural = _('Series_Seasons')


class FilmSeriesVideoModel(models.Model):
    title = models.CharField(max_length=50, verbose_name=_('title'))
    season = models.ForeignKey(
        FilmSeriesSeasonModel, on_delete=models.CASCADE, related_name='videos', verbose_name=_('season')
    )
    video = models.FileField(upload_to='series', verbose_name=_('video'))
    cover = models.ImageField(upload_to='series_cover', verbose_name=_('cover'), default='/static/img/covers/cover.jpg')
    created_at = models.DateField(verbose_name=_('created_at'), default=12)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Season_series')
        verbose_name_plural = _('Season_TV_series')
