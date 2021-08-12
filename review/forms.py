from django import forms

from review.models import FilmCommentModel, SeriesCommentModel, ReviewModel, LikeModel, SeriesCommentLikeModel


class FilmCommentFormModel(forms.ModelForm):
    class Meta:
        model = FilmCommentModel
        exclude = ['film', 'user', 'unliked', 'liked']


class SeriesCommentFormModel(forms.ModelForm):
    class Meta:
        model = SeriesCommentModel
        exclude = ['series', 'user', 'unliked', 'liked']


class FilmRatingFormModel(forms.ModelForm):
    class Meta:
        model = ReviewModel
        exclude = ['film', 'user']


class LikeCommentFormModel(forms.ModelForm):
    """Film Comment LikeFormModel"""

    class Meta:
        model = LikeModel
        fields = ['comments']


class SeriesLikeCommentFormModel(forms.ModelForm):
    """Series Comment LikeFormModel"""

    class Meta:
        model = SeriesCommentLikeModel
        fields = ['comments']
