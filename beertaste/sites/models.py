from django.db import models
from stdimage import StdimageField, JPEGField
from stdimage.validators import MinSizeValidator

# Create your models here.
class beerReview(models.Model):
    beer_name = models.CharField(max_lenght=200)
    starts = models.IntegerField()
    image = JPEGField(upload_to='images/', blank=false, variations={
    'thumbnail':(400, 400, True)}, delete_orphans=True, validators=[MinSizeValidator(400,400)])
    drank_date = models.DateTimeField('data published', auto_now_add=True)
    description = models.CharField(max_lenght=250)

#Maybe small brief for
