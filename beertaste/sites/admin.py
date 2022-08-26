from django.contrib import admin
from .models import beerReview

# Register your models here.
#Look more ways to make admin-page look better from django doc.
class beerReviewAdmin(admin.ModelAdmin):
    list_display = ("beer_name", "image", "stars", "drank_date")
    search_fields = ["description"]

admin.site.register(beerReview, beerReviewAdmin)
