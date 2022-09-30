from django import forms
from .models import beerReview, tags, country, mold
from stdimage.validators import MinSizeValidator

#Might write this without using Meta and in views rip data from form to model!
class UploadReview(forms.ModelForm):
    #class Meta lets us use model for form
    class Meta:
        model = beerReview
        fields = ["beer_name", "stars", "image", "description", "adjectives", "beer_type","countryMade"]

# Test This later. Might need to some how import adjectives, beer_type and country.
# This ain't ModelForm, because we aint using model here
class radioReview(forms.Form):
    numberChoice = (
        (1,"1"),
        (2,"2"),
        (3,"3"),
        (4,"4"),
        (5,"5"),
        (6,"6"),
        (7,"7"),
        (8,"8"),
        (9,"9"),
        (10,"10"),
        )
    name = forms.CharField(label="Beer name:")
    stars = forms.ChoiceField(choices=numberChoice, widget=forms.RadioSelect())
    image = forms.ImageField(validators=[MinSizeValidator(400,400)])
    description = forms.CharField(max_length=300)
    adjectives = forms.ModelMultipleChoiceField(queryset=tags.objects.all())
    country = forms.ModelChoiceField(queryset=country.objects.all())
    mold = forms.ModelChoiceField(queryset=mold.objects.all())
