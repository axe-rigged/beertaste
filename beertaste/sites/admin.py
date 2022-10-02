from django.contrib import admin
from .models import beerReview, tags, country, mold

# Register your models here.
#Look more ways to make admin-page look better from django doc.
# This names are verybad
class beerReviewAdmin(admin.ModelAdmin):
    list_display = ("beer_name", "image", "stars", "drank_date")
    search_fields = ["description"]

class tagsForBeer(admin.ModelAdmin):
    list_display = ["adjective"]

class beerHome(admin.ModelAdmin):
    list_display = ["country_name"]

class beerMold(admin.ModelAdmin):
    list_display = ["typeOfBeer"]

admin.site.register(beerReview, beerReviewAdmin)
admin.site.register(tags, tagsForBeer)
admin.site.register(country, beerHome)
admin.site.register(mold, beerMold)
