from django import forms

from .models import Review


REVIEW_POINT_CHOICES = (("1", 1), ("2", 2), ("3", 3), ("4", 4), ("5", 5))


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "point",
            "content",
        ]
        labels = {"point": ("평점"), "content": ("리뷰를 남겨주세요.")}

        widgets = {
            "content": forms.TextInput(),
            "point": forms.Select(choices=REVIEW_POINT_CHOICES),
        }
