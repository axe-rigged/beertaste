from django.db import models
from stdimage import StdImageField, JPEGField
from stdimage.validators import MinSizeValidator

#County where it is made
class country(models.Model):
    country_name = models.CharField(max_length=100)

    def __str__(self):
        return self.country_name

#Tags to be used for beer
class tags(models.Model):
    adjective = models.CharField(max_length=100)

    def __str__(self):
        return self.adjective

#Type of beer (add later)
class mold(models.Model):
    typeOfBeer = models.CharField(max_length=100)

    def __str__(self):
        return self.typeOfBeer

# Create your models here.
# Add default values for image and stars.
# Need to make one good migrate
class beerReview(models.Model):

    starsChoice = (
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

    beer_name = models.CharField(max_length=200)
    stars = models.IntegerField(choices=starsChoice)
    image = JPEGField(upload_to='images/', blank=False, variations={
    'thumbnail':(400, 400, True)}, delete_orphans=True, validators=[MinSizeValidator(400,400)])
    drank_date = models.DateTimeField('data published', auto_now_add=True)
    description = models.CharField(max_length=300)
    adjectives = models.ManyToManyField(tags)
    beer_type = models.ForeignKey(mold, on_delete=models.CASCADE, null=True)
    countryMade = models.ForeignKey(country, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.beer_name
