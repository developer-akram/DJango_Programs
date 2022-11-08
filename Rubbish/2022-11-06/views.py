from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student
def home(request):
    return render(request,"website/home.html")

def about(request):
    if request.method=="POST":
        name = request.POST["txtname"]
        gen = request.POST["gen"]
        btnsubmit = request.POST["btnsubmit"]
        course = request.POST.getlist("course")
        course1=""
        for c in course:
            course1 += c + " "
        country = request.POST["country"]
        state  = request.POST.getlist("state")
        state1=""
        for c in state:
            state1 += c + " "
        msg = request.POST["message"]    
        return render(request,"website/about.html",{"name":name,"gender":gen,"course":course1,"country":country,"state":state1,"message":msg,"btn":btnsubmit})    



    return render(request,"website/about.html")

def services(request):
    if request.method=="POST":
        rno = request.POST["txtrno"]
        name = request.POST["txtname"]
        branch = request.POST["txtbranch"]
        fees = request.POST["txtfees"]
        obj = Student(rno=rno,name=name,branch=branch,fees=fees)
        obj.save()
        return render(request,"website/services.html",{"key":"Student Data Submitted Successfully"}) 

    return render(request,"website/services.html")   

def gallery(request):
    data = Student.objects.all()
    return render(request,"website/gallery.html",{"res":data}) 
def findstu(request):
    data = Student.objects.get(pk=request.GET["q"])
    if request.method=="POST":
       data.rno = request.POST["txtrno"]
       data.name = request.POST["txtname"]
       data.branch = request.POST["txtbranch"]
       data.fees = request.POST["txtfees"]
       data.save()
       return redirect('gallery')
    

    
    return render(request,"website/findstu.html",{"stu":data}) 
def contact(request):
    if request.method=="POST":
        return HttpResponse("Welcome in Contact Form")
    return render(request,"website/contact.html")       

