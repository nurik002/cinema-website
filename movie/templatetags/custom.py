from django.shortcuts import get_object_or_404
from django.template import Library

from movie.models import FilmSeriesVideoModel

register = Library()


@register.simple_tag
def get_series_chapter(request, serial):
    season = request.GET.get('season')
    chapter = request.GET.get('chapter')

    if season and chapter:
        obj = get_object_or_404(FilmSeriesVideoModel, pk=chapter, season_id=season)
        return obj.video.url
    else:
        season = serial.season.first()
        chapter = season.videos.first()
        return chapter.video.url
