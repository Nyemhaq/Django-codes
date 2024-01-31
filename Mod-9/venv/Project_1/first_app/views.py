from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (req):
    return HttpResponse("This is first app page")

def courses (req):
    return HttpResponse("This is first app courses page")

def about (req):
    return HttpResponse("This is first app about page")