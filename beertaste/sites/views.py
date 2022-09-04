from django.shortcuts import render, redirect
from .models import beerReview
from .forms import UploadReview

def beerIndex(request):
    # Add later POST in dialog/popup way
    #if request.method == "POST":
    #    #Validate that post is legit and then return index With get.
    #   form = UploadReview(request.POST, request.FILES)
    #   if form.is_valid:
    #       review = form.save(commit=False)
    #       #We later need to check start and maybe something else
    #       review.save()
    #       return redirect("sites:beerIndex")
    # Check if this redirect works to get GET, read documents
    #else:
    #    form = UploadReview()
    if request.method == "GET":
        beer = beerReview.objects.all()
        return render(request, "sites/index.html", {"beer" : beer})

def uploadBeer(request):
    if request.method == "POST":
        form = UploadReview(request.POST, request.FILES)
        if form.is_valid:
            review = form.save(commit=False)
            #We later need to check start and maybe something else
            review.save()
            return redirect("sites:beerIndex")
    else:
        form = UploadReview()
    return render(request, "sites/upload.html", {"form":form})
