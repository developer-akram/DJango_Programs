from django.shortcuts import render

def index(request):
    return render(request, 'siteone/index.html')

def about(request):
    return render(request, 'siteone/about.html')

def contact(request):
    return render(request, 'siteone/contact.html')

def services(request):
    return render(request, 'siteone/services.html')

def shop(request):
    return render(request, 'siteone/shop.html')

# Create your views here.
