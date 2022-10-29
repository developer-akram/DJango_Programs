from django.shortcuts import render


def index(request):
    return render(request, 'sitetwo/index.html')

def about(request):
    return render(request, 'sitetwo/about.html')

def contact(request):
    return render(request, 'sitetwo/contact.html')

def service(request):
    return render(request, 'sitetwo/service.html')

def team(request):
    return render(request, 'sitetwo/team.html')

def detail(request):
    return render(request, 'sitetwo/detail.html')

def blog(request):
    return render(request, 'sitetwo/blog.html')

def testimonial(request):
    return render(request, 'sitetwo/testimonial.html')
# Create your views here.
