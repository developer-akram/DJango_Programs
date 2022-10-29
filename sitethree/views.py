from django.shortcuts import render


def index(request):
    return render(request, 'sitethree/index.html')

def about(request):
    return render(request, 'sitethree/about.html')

def contact(request):
    return render(request, 'sitethree/contact.html')

def feature(request):
    return render(request, 'sitethree/feature.html')

def team(request):
    return render(request, 'sitethree/team.html')

def detail(request):
    return render(request, 'sitethree/detail.html')

def course(request):
    return render(request, 'sitethree/course.html')

def testimonial(request):
    return render(request, 'sitethree/testimonial.html')

# Create your views here.
