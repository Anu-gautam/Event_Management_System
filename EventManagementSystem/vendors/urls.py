from django.contrib import admin
from django.urls import path
from vendors import views

urlpatterns = [ 
    path('', views.main, name="home")
    # path('vendor', views.index, name="vendor"),
]