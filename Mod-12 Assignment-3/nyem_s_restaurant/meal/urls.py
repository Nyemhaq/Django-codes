from django.urls import path
from . import views

urlpatterns = [
    path('', views.meal, name='show_item'),
]
