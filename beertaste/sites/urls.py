from django.urls import path
from . views import beerIndex

app_name = "sites"
urlpatterns = [
        path("", beerIndex, name="beerIndex")
]
