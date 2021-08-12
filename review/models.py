from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
from movie.models import FilmModel, FilmSeriesModel
from django.utils.translation import gettext_lazy as _

UserModel = get_user_model()


class ReviewModel(models.Model):
    """Review"""
    film = models.ForeignKey(FilmModel, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=100, verbose_name=_('title'), blank=True, null=True)
    review = models.TextField(verbose_name=_('review'), blank=True, null=True)
    rating = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)],
                                         verbose_name=_('rating'))
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='rating', verbose_name=_('user'))

    class Meta:
        verbose_name = _('review')
        verbose_name_plural = _('reviews')


class AbstractCommentModel(models.Model):
    """Comment AbstractModel"""
    text = models.TextField(verbose_name=_('text'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))
    liked = models.IntegerField(default=0, verbose_name=_('liked'))
    unliked = models.IntegerField(default=0, verbose_name=_('unliked'))

    def __str__(self):
        return self.text

    class Meta:
        abstract = True


class FilmCommentModel(AbstractCommentModel):
    """Film CommentModel"""
    film = models.ForeignKey(FilmModel, on_delete=models.CASCADE, related_name='film_comments', verbose_name=_('film'))
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="film_comments_user",
                             verbose_name=_('user'))

    class Meta:
        verbose_name = _('film_comment')
        verbose_name_plural = _('films_comments')


class SeriesCommentModel(AbstractCommentModel):
    """Series CommentModel"""
    series = models.ForeignKey(FilmSeriesModel, on_delete=models.CASCADE, related_name='series_comments',
                               verbose_name=_('series'))
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="series", verbose_name=_('user'))

    class Meta:
        verbose_name = _('series_comment')
        verbose_name_plural = _('series_comments')


class LikeModel(models.Model):
    """Film LikeModel"""
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="like_user", verbose_name=_('user'))
    type_like = models.IntegerField(default=0, verbose_name=_('type_like'))
    comments = models.ForeignKey(FilmCommentModel, on_delete=models.CASCADE, related_name='like_comments')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    class Meta:
        verbose_name = _('like')
        verbose_name_plural = _('likes')

    def __str__(self):
        return str(self.user)


class SeriesCommentLikeModel(models.Model):
    """Series Comment LikeModel"""
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="series_like_user",
                             verbose_name=_('user'))
    type_like = models.IntegerField(default=0, verbose_name=_('type_like'))
    comments = models.ForeignKey(SeriesCommentModel, on_delete=models.CASCADE, related_name='series_like_comments')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('created_at'))

    class Meta:
        verbose_name = _('Series_like')
        verbose_name_plural = _('Series_likes')

    def __str__(self):
        return str(self.user)
