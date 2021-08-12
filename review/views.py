from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

# Film Comment CreateView
from django.urls import reverse
from django.views.generic import CreateView

from movie.models import FilmModel, FilmSeriesModel
from review.forms import FilmCommentFormModel, SeriesCommentFormModel, FilmRatingFormModel, SeriesLikeCommentFormModel, \
    LikeCommentFormModel
from review.models import FilmCommentModel, LikeModel, SeriesCommentModel, SeriesCommentLikeModel


class CommentCreateView(LoginRequiredMixin, CreateView):
    """Comment CreatView"""

    def get_form_class(self, form_class=None):
        cat = self.kwargs.get('category')
        if cat == 'series':
            return SeriesCommentFormModel
        return FilmCommentFormModel

    def get_success_url(self):
        return reverse('movie:movie-detail',
                       kwargs={'category': self.kwargs.get('category'), 'pk': self.kwargs.get('pk')})

    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        cat = self.kwargs.get('category')
        if cat == 'series':
            form.instance.series = get_object_or_404(FilmSeriesModel, pk=pk)
        else:
            form.instance.film = get_object_or_404(FilmModel, pk=pk)

        form.instance.user = self.request.user
        return super(CommentCreateView, self).form_valid(form)


class FilmRatingCrateView(CreateView):
    """Rating Crate"""
    form_class = FilmRatingFormModel

    def get_success_url(self):
        return reverse('movie:movie-detail', kwargs={'pk': self.kwargs.get('pk')})

    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        form.instance.film = get_object_or_404(FilmModel, pk=pk)
        form.instance.user = self.request.user
        return super(FilmRatingCrateView, self).form_valid(form)


class LikeCommentCrateView(LoginRequiredMixin, CreateView):
    """Comment Like CrateView"""

    def get_form_class(self):
        cat = self.kwargs.get('category')
        if cat == 'series':
            return SeriesLikeCommentFormModel
        return LikeCommentFormModel

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def get_success_url(self):
        return self.request.GET.get('next', '/')
        # return reverse('movie:movie-detail', kwargs={'category': self.kwargs.get('category'), 'pk':})

    def form_valid(self, form):
        cat = self.kwargs.get('category')
        comment_id = self.request.POST.get('comments')
        user = self.request.user
        if cat == 'series':
            seris_comment = get_object_or_404(SeriesCommentModel, pk=comment_id)
            current_like = seris_comment.liked
            like_comment = SeriesCommentLikeModel.objects.filter(type_like=2, comments=seris_comment,
                                                                 user=user).exists()
            if not like_comment:
                SeriesCommentLikeModel.objects.create(type_like=2, comments=seris_comment, user=user)
                current_like = current_like + 1
            else:
                SeriesCommentLikeModel.objects.filter(type_like=2, comments=seris_comment, user=user).delete()
                current_like = current_like - 1
            seris_comment.liked = current_like
            seris_comment.save()
        else:
            film_comment = get_object_or_404(FilmCommentModel, pk=comment_id)
            current_like = film_comment.liked
            like_comment = LikeModel.objects.filter(type_like=2, comments=film_comment, user=user).count()
            if not like_comment:
                LikeModel.objects.create(type_like=2, comments=film_comment, user=user)
                current_like = current_like + 1
            else:
                LikeModel.objects.filter(type_like=2, comments=film_comment, user=user).delete()
                current_like = current_like - 1
            film_comment.liked = current_like
            film_comment.save()
        return redirect(self.get_success_url())
        # return super(LikeCommentCrateView, self).form_valid(form)


class UnLikeCommentCrateView(LoginRequiredMixin, CreateView):
    """Comment Unlike CreateView"""

    def get_form_class(self):
        cat = self.kwargs.get('category')
        if cat == 'series':
            return SeriesLikeCommentFormModel
        return LikeCommentFormModel

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def get_success_url(self):
        return self.request.GET.get('next', '/')
        # return reverse('movie:movie-detail', kwargs={'category': self.kwargs.get('category'), 'pk':})

    def form_valid(self, form):
        cat = self.kwargs.get('category')
        comment_id = self.request.POST.get('comments')
        user = self.request.user
        if cat == 'series':
            series_comment = get_object_or_404(SeriesCommentModel, pk=comment_id)
            current_unlike = series_comment.unliked
            unlike_comment = SeriesCommentLikeModel.objects.filter(type_like=1, comments=series_comment,
                                                                   user=user).exists()
            current_like = series_comment.liked
            like_comment = SeriesCommentLikeModel.objects.filter(type_like=2, comments=series_comment,
                                                                 user=user).exists()
            if not unlike_comment and not like_comment:
                SeriesCommentLikeModel.objects.create(type_like=1, comments=series_comment, user=user)
                current_unlike = current_unlike + 1
            elif like_comment and not unlike_comment:
                SeriesCommentLikeModel.objects.filter(type_like=2, comments=series_comment, user=user).delete()
                current_like = current_like - 1
                SeriesCommentLikeModel.objects.create(type_like=1, comments=series_comment, user=user)
                current_unlike = current_unlike + 1
                series_comment.liked = current_like
            else:
                SeriesCommentLikeModel.objects.filter(type_like=1, comments=series_comment, user=user).delete()
                current_unlike = current_unlike - 1
            series_comment.unliked = current_unlike
            series_comment.save()
        else:
            film_comment = get_object_or_404(FilmCommentModel, pk=comment_id)
            current_unlike = film_comment.unliked
            current_like = film_comment.liked
            unlike_comment = LikeModel.objects.filter(type_like=1, comments=film_comment, user=user).count()
            like_comment = LikeModel.objects.filter(type_like=2, comments=film_comment, user=user).count()
            if not unlike_comment and not like_comment:
                LikeModel.objects.create(type_like=1, comments=film_comment, user=user)
                current_unlike += 1
            elif like_comment and not unlike_comment:
                LikeModel.objects.filter(type_like=2, comments=film_comment, user=user).delete()
                current_like -= 1
                LikeModel.objects.create(type_like=1, comments=film_comment, user=user)
                current_unlike += 1
                film_comment.liked = current_like
            else:
                LikeModel.objects.filter(type_like=1, comments=film_comment, user=user).delete()
                current_unlike -= 1
            film_comment.unliked = current_unlike
            film_comment.save()
        return redirect(self.get_success_url())
        # return super(LikeCommentCrateView, self).form_valid(form)



