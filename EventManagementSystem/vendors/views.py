from django.shortcuts import render, HttpResponse


# Create your views here.

def main(request):
    return render(request, "main.html")

def index(request):
    
    return render(request, "index.html")

# def about(request):
#     return render(request, "about.html")

# def services(request):
#     return render(request, "services1.html")

# def contact(request):
#     return render(request, "contact.html")

# def product(request):
#     return render(request, "product.html")