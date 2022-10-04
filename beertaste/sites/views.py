from django.shortcuts import render, redirect, get_object_or_404
from .models import beerReview
from .forms import UploadReview, radioReview

# model.object needs to use .all() or .get(id/pk). And on template we need to use object.all
def beerIndex(request):
    if request.method == "GET":
        beer = beerReview.objects.all()
        return render(request, "sites/index.html", {"beer" : beer})

# Image files need to have .image_file like *.jpeg or *.png
def uploadBeer(request):
    if request.method == "POST":
        form = UploadReview(request.POST, request.FILES)
        if form.is_valid:
            review = form.save(commit=False)
            review.save()
            return redirect("sites:beerIndex")
    else:
        form = UploadReview()
    return render(request, "sites/upload.html", {"form":form})

# This is test that can I make form and use it without using form.model.
# TEST
def testUploadBeer(request):
    if request.method == "POST":
        form = radioReview(request.POST, request.FILES)
        if form.is_valid:
            print(form)
    else:
        form = radioReview()
    return render(request, "sites/upT.html", {"form":form})
# TEST

#url "<pk:int/>". Check if request has pk in it or does it need to be told
#(modelsName, pk/slug/etc = url pk/slug/etc)
def beerInfo(request, pk):
    if request.method == "GET":
        theBeer = get_object_or_404(beerReview, pk=pk)
        return render(request, "sites/beer.html", {"theBeer": theBeer})
