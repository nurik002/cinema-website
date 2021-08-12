from modeltranslation.translator import register, TranslationOptions

from movie.models import GenreModel, FilmModel, FilmSeriesModel, CategoryModel


@register(GenreModel)
class GenreTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(CategoryModel)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(FilmModel)
class FilmTranslationOptions(TranslationOptions):
    fields = ('title', 'country', 'description',)


@register(FilmSeriesModel)
class FilmSeriesTranslationOptions(TranslationOptions):
    fields = ('title', 'country', 'description',)
