from django.db import models
from stdimage import StdImageField, JPEGField
from stdimage.validators import MinSizeValidator

# Create your models here.
class beerReview(models.Model):
    beer_name = models.CharField(max_length=200)
    stars = models.IntegerField()
    image = JPEGField(upload_to='images/', blank=False, variations={
    'thumbnail':(400, 400, True)}, delete_orphans=True, validators=[MinSizeValidator(400,400)])
    drank_date = models.DateTimeField('data published', auto_now_add=True)
    description = models.CharField(max_length=250)

#Maybe small brief for
