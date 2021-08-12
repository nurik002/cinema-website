from django.contrib import admin

# Register your models here.
from review.models import FilmCommentModel, LikeModel, SeriesCommentModel, ReviewModel, SeriesCommentLikeModel


@admin.register(ReviewModel)
class ReviewAdminModel(admin.ModelAdmin):
    list_display = ['user', 'title', 'rating']
    list_filter = ['film']


@admin.register(FilmCommentModel)
class FilmCommentsAdminModel(admin.ModelAdmin):
    list_display = ['user', 'film', 'text']
    list_filter = ['film']
    readonly_fields = ['liked', 'unliked']


@admin.register(SeriesCommentModel)
class SeriesCommentsAdminModel(admin.ModelAdmin):
    list_display = ['user', 'series', 'text']
    list_filter = ['series']
    # readonly_fields = ['liked', 'unliked']


@admin.register(LikeModel)
class LikeAdminModel(admin.ModelAdmin):
    list_display = ['user', 'comments']
    list_filter = ['user', 'comments']


@admin.register(SeriesCommentLikeModel)
class LikeAdminModel(admin.ModelAdmin):
    list_display = ['user', 'comments']
    list_filter = ['user', 'comments']
