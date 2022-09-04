from django.urls import path
from . views import *

app_name = "sites"
urlpatterns = [
        path("", beerIndex, name = "beerIndex"),
        path("upload", uploadBeer, name = "uploadBeer")
]
