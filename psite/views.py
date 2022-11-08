from django.shortcuts import render

def index(request):
    return render(request, 'psite/index.html')

def about(request):
    return render(request, 'psite/about.html')

def contact(request):
    return render(request, 'psite/contact.html')

def products(request):
    return render(request, 'psite/products.html')

def blog(request):
    return render(request, 'psite/blog.html')

# Create your views here.
