from django.contrib import admin
from .models import beerReview, tags, country

# Register your models here.
#Look more ways to make admin-page look better from django doc.
class beerReviewAdmin(admin.ModelAdmin):
    list_display = ("beer_name", "image", "stars", "drank_date")
    search_fields = ["description"]

class tagsForBeer(admin.ModelAdmin):
    list_display = ("adjective")

class beerHome(admin.ModelAdmin):
    list_display = ("country_name")

admin.site.register(beerReview, beerReviewAdmin)
