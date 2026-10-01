from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    s="<h1>This is Sistec Page." \
    "Sagar Institute of Science & Technology (SISTec), " \
    "Gandhi Nagar is a premier engineering and management institution located opposite the Raja Bhoj International Airport in Gandhi Nagar," \
    " Bhopal, Madhya Pradesh.</h1>"
    return HttpResponse(s)
