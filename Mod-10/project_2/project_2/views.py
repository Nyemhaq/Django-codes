from django.http import HttpResponse
from django.shortcuts import render

def home (req):
    return HttpResponse("This is Home page")

def index(req):
    return render (req, 'index.html')

def new (req):
    return render (req, 'new.html')