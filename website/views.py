from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Student,Register
def home(request):
    if request.method=="POST":
        obj = Register(username=request.POST["txtuser"],password=request.POST["txtpass"],email=request.POST["txtemail"],mobile=request.POST["txtmobile"])
        obj.save()
        return render(request,"website/home.html",{"key":"registration successfully"})
    return render(request,"website/home.html")
def login(request):
    if request.method=="POST":
        obj = Register.objects.filter(username=request.POST["txtuser"],password=request.POST["txtpass"])
        if(obj.count()>0):
          request.session["loggedid"] = request.POST["txtuser"]
          return redirect('gallery')
        else:
         return render(request,"website/login.html",{"key":"Invalid userid and password"})      
        
    return render(request,"website/login.html")
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
        return redirect('gallery')
       #return render(request,"website/services.html",{"key":"Student Data Submitted Successfully"}) 

    return render(request,"website/services.html")   

def gallery(request):
    if request.session.has_key("loggedid"):
       data = Student.objects.all()
       data1 = Register.objects.filter(username=request.session["loggedid"])
       return render(request,"website/gallery.html",{"res":data,"res1":data1}) 
    else:
        return redirect('/website/login')   
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
def deletestu(request):
    data = Student.objects.get(pk=request.GET["q"])
    if request.method=="POST":
        data.delete()
        return redirect('gallery')
    return render(request,"website/deleteconfirmation.html",{"res":data})

    

    
    return render(request,"website/findstu.html",{"stu":data}) 
def contact(request):
    if request.method=="POST":
        return HttpResponse("Welcome in Contact Form")
    return render(request,"website/contact.html")       

def logout(request):
    del request.session["loggedid"]
    return redirect("login")