from django.urls import path
from .views import vendor_dashboard, add_item, create_vendor

urlpatterns = [
    path('', vendor_dashboard, name='vendor_dashboard'),
    path('add_item/', add_item, name='add_item'),
    path('create_vendor/', create_vendor, name='create_vendor'),
]