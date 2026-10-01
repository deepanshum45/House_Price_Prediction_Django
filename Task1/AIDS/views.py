from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dept(request):
    s="""<h1>This is a AIDS Page.
    The Head of the Department (HOD) for the Computer Science & Engineering with Artificial Intelligence & Data Science 
    (CSE-AIDS) department at Sagar Institute of Science & Technology (SISTec) Gandhi Nagar is Dr Vasima Khan<h1>"""
    return HttpResponse(s)