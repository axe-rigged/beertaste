from django.db import models
from stdimage import StdImageField, JPEGField
from stdimage.validators import MinSizeValidator

#County where it is made
class country(models.Model):
    country_name = models.CharField(max_length=100)

#Tags to be used for beer
class tags(models.Model):
    adjective = models.CharField(max_length=100)

#Type of beer (add later)
class mold(models.Model):
    typeOfBeer = models.CharField(max_length=100)

# Create your models here.
# Maybe change "stars" integer to choice. So we can press 1-10 radio buttons for choice. Maybe in forms easier
class beerReview(models.Model):
    beer_name = models.CharField(max_length=200)
    stars = models.IntegerField()
    image = JPEGField(upload_to='images/', blank=False, variations={
    'thumbnail':(400, 400, True)}, delete_orphans=True, validators=[MinSizeValidator(400,400)])
    drank_date = models.DateTimeField('data published', auto_now_add=True)
    description = models.CharField(max_length=300)
    adjectives = models.ManyToManyField(tags)
    beer_type = models.ForeignKey(mold, on_delete=models.CASCADE, null=True)
    countryMade = models.ForeignKey(country, on_delete=models.CASCADE, null=True)

