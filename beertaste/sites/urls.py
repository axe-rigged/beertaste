from django.urls import path
from . views import *

app_name = "sites"
# Add later typing for variables
urlpatterns = [
        path("", beerIndex, name = "beerIndex"),
        path("upload", uploadBeer, name = "uploadBeer"),
        path("<pk>/beer", beerInfo, name = "beerInfo"),
]
