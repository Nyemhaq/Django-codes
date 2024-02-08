from django.shortcuts import render
from django.http import HttpResponse

def home (req):
    return HttpResponse("This is app home")

def about(req):
    return render (req, "navigation/about.html")

def contact(req):
    return render (req, "navigation/contact.html")
