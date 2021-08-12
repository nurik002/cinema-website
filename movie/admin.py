from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from movie.models import GenreModel, FilmModel, FilmSeriesModel, FilmSeriesVideoModel, FilmSeriesSeasonModel, \
    CategoryModel, QualityModel


class MyTranslation(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(GenreModel)
class AdminGenreModel(MyTranslation):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(CategoryModel)
class AdminCategoryModel(MyTranslation):
    list_display = ['title', 'created_at']


@admin.register(QualityModel)
class AdminQualityModel(admin.ModelAdmin):
    list_display = ['title', 'created_at']


#
class SeriesModelInline(admin.TabularInline):
    model = FilmSeriesVideoModel


@admin.register(FilmModel)
class FilmAdminModel(MyTranslation):
    list_display = ['title', 'category', 'release_year', 'country', 'created_at']
    list_filter = ['genre', 'category']
    search_fields = ['name', 'category', 'release_year', 'country']
    readonly_fields = ['rating']


@admin.register(FilmSeriesSeasonModel)
class FimSeriesSeasonModelAdmin(admin.ModelAdmin):
    list_display = ['series', 'season']
    inlines = [SeriesModelInline]


@admin.register(FilmSeriesModel)
class FilmSeriesAdminModel(MyTranslation):
    list_display = ['title', 'rating', 'release_year', 'country', 'created_at']
    list_filter = ['genre']
    search_fields = ['name', 'release_year', 'country']
    readonly_fields = ['rating']



