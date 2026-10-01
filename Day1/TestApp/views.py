from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def greet(request):
    s="<h1>My Name is Deepanshu Mehra</h1>"

    return HttpResponse(s)