from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dep(request):
    s="<h1>This is CS page:" \
    "The Head of the Department (HOD) for Computer Science & Engineering " 
    "at the Sagar Institute of Science & Technology (SISTec) " 
    "Gandhi Nagar campus in Bhopal is Mr. Nargish Gupta</h1>"
    return HttpResponse(s)
