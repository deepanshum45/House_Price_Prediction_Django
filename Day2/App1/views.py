from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    s="<h1>This is a home page:</h1>"

    return HttpResponse(s)

def about(request):
    s="<h1>this is about page:</h1>"

    return HttpResponse(s)
