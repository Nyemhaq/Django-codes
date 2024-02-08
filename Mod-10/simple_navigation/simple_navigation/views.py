from django.http import HttpResponse
from django.shortcuts import render

def home (req):
    # return HttpResponse("This is Home page")
    d={'Name':'Nayeem','age': 14,'lst':[1,2,3],
        'courses':[{'id': 1 , 'Name':'Python', 'Fee':3000},
                   {'id': 2 , 'Name':'Django', 'Fee':5000},
                   {'id': 3 , 'Name':'C', 'Fee':1500}] ,      
      }
    return render (req, "home.html", d) #we can also write as context=d 