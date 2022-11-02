from django.shortcuts import render
def index(request):
    return render(request,"mical/index.html")
def about(request):
    return render(request,"mical/about.html")   

def furnitures(request):
    pass       
def testimonial(request):
    pass  
def contacts(request):
    pass  
