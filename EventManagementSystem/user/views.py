from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Order
from vendors.models import Item, Vendor

def user_dashboard(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'user/dashboard.html', {'orders': orders})

def add_to_cart(request, item_id):
    item = Item.objects.get(id=item_id)
    order = Order(user=request.user, item=item, quantity=1)
    order.save()
    return redirect('user_dashboard')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create a Vendor instance for the new user
            Vendor.objects.create(user=user, shop_name="Default Shop Name")  # You can customize the shop name
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})