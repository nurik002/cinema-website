from itertools import chain

from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, TemplateView, DetailView, CreateView
from django.utils.translation import ugettext_lazy as _

from movie.models import GenreModel, QualityModel, FilmModel, FilmSeriesModel
from review.models import FilmCommentModel, LikeModel


class MovieTemplateView(TemplateView):
    """Index.html TemplateView"""
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(MovieTemplateView, self).get_context_data(**kwargs)
        context['new_season'] = FilmModel.objects.filter(release_year=2021)
        context['films'] = FilmModel.objects.filter(Q(category__title='Films') | Q(category__title='Фильмы')).order_by(
            '-pk')
        context['series'] = FilmSeriesModel.objects.order_by('-pk')
        context['cartoons'] = FilmModel.objects.filter(
            Q(category__title='Cartoons') | Q(category__title='Мультфильмы')).order_by('-pk')
        return context


class MovieListView(ListView):
    """Movie ListView"""
    template_name = 'catalog1.html'

    # paginate_by = 4

    def get_queryset(self):
        qs = FilmModel.objects.order_by('-pk')
        q = self.request.GET.get('q')
        quality = self.request.GET.get('quality')
        genre = self.request.GET.get('genre')
        category = self.kwargs.get('category')
        if category == 'series':
            qs = FilmSeriesModel.objects.all()
        elif category == 'cartoon':
            qs = qs.filter(Q(category__title='Cartoons') | Q(category__title='Мультфильмы'))
        else:
            qs = qs.filter(Q(category__title='Films') | Q(category__title='Фильмы'))
        if quality:
            qs = qs.filter(quality_id=quality)
        if genre:
            qs = qs.filter(genre__id=genre)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['genre'] = GenreModel.objects.all()
        context['quality'] = QualityModel.objects.all()
        return context


class SearchListView(ListView):
    template_name = 'catalog1.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SearchListView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self):
        query = self.request.GET.get('q', None)

        if query is not None:
            films_results = FilmModel.objects.search(query)
            series_results = FilmSeriesModel.objects.search(query)

            queryset_chain = chain(films_results, series_results)

            qs = sorted(queryset_chain, key=lambda instance: instance.pk, reverse=True)
        return qs


class TotalDetailView(DetailView):
    template_name = 'details1.html'

    def get_object(self, queryset=None):
        cat = self.kwargs.get('category')
        pk = self.kwargs.get('pk')

        if cat == 'films' or cat == 'cartoon':
            obj = get_object_or_404(FilmModel, pk=pk)
        elif cat == 'series':
            obj = get_object_or_404(FilmSeriesModel, pk=pk)
        else:
            raise Http404

        return obj

    def get_context_data(self, **kwargs):
        context = super(TotalDetailView, self).get_context_data(**kwargs)
        # context['related_genre'] = FilmModel.objects.filter(genre__in=self.object.genre)
        return context
