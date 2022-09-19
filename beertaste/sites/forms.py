from django import forms
from .models import beerReview

class UploadReview(forms.ModelForm):
    class Meta:
        model = beerReview
        fields = ["beer_name", "stars", "image", "description", "adjectives", "beer_type","countryMade"]
