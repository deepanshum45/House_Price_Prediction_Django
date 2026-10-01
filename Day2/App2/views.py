from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def instagram(request):
    s="<h1>This is a instagram page:</h1>"

    return HttpResponse(s)

def linkdin(request):
    s="<h1>this is linkedin page:</h1>"

    return HttpResponse(s)