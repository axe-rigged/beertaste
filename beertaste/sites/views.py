from django.shortcuts import render

def beerIndex(request):
    return render(request, "sites/index.html", {})
