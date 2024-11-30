from django.urls import path
from .views import user_dashboard, add_to_cart

urlpatterns = [
    path('', user_dashboard, name='user_dashboard'),
    path('add_to_cart/<int:item_id>/', add_to_cart, name='add_to_cart'),
]