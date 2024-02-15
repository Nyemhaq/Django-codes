from django.shortcuts import render

def about_us (req):
    return render (req, 'about/about_us.html')
