from django.shortcuts import render

def about_us (req):
    return render (req, 'about_us/about_us.html' )
