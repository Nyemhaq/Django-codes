from django.contrib import admin
from django.urls import path, include
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', view.contact),
    path("", view.home),
    path("first_app/", include("first_app.urls")),
]
