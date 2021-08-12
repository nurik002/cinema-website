from django.urls import path

from review.views import CommentCreateView, FilmRatingCrateView, LikeCommentCrateView, UnLikeCommentCrateView

app_name = 'review'
urlpatterns = [
    path('film-comment/<str:category>/<int:pk>', CommentCreateView.as_view(), name='film-comment'),
    path('like/<str:category>/', LikeCommentCrateView.as_view(), name='like'),
    path('unlike/<str:category>/', UnLikeCommentCrateView.as_view(), name='unlike'),
    # path('series-comment/<int:pk>', FilmSeriesCommentCreateView.as_view(), name='series-comment'),
    path('film-rating/<int:pk>', FilmRatingCrateView.as_view(), name='film-rating'),
]
