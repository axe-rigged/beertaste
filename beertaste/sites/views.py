from django.shortcuts import render, redirect
from .models import beerReview
from .forms import UploadReview

def beerIndex(request):
    if request.method == "POST":
        #Validate that post is legit and then return index With get.
       form = UploadReview(request.POST, request.FILES)
       if form.is_valid:
           review = form.save(commit=False)
           #We later need to check start and maybe something else
           review.save()
           return redirect("sites:index")
    else:
        form = UploadReview()
    if request.method == "GET":
        return render(request, "sites/index.html", {"form" : form})
