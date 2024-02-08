from django.shortcuts import render
from django.http import HttpResponse

def home (req):
    # return HttpResponse("This is app Home")
    return render (req, 'first_app/home.html')
