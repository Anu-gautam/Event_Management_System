from django.shortcuts import render, redirect
from .models import Item, Vendor
from .forms import ItemForm

# def vendor_dashboard(request):
#     items = Item.objects.filter(vendor=request.user.vendor)
#     return render(request, 'vendor/dashboard.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.vendor = request.user.vendor
            item.save()
            return redirect('vendor_dashboard')
    else:
        form = ItemForm()
    return render(request, 'vendors/add_item.html', {'form': form})



def vendor_dashboard(request):
    if not hasattr(request.user, 'vendor'):
        return redirect('create_vendor')  # Redirect to a view where they can create a vendor

    items = Item.objects.filter(vendor=request.user.vendor)
    return render(request, 'vendors/dashboard.html', {'items': items})

def create_vendor(request):
    if request.method == 'POST':
        shop_name = request.POST.get('shop_name')
        Vendor.objects.create(user=request.user, shop_name=shop_name)
        return redirect('vendor_dashboard')
    return render(request, 'vendors/create_vendor.html')