from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.urls import reverse
from .models import Job
class Add(View):
   def get(self,request): 
       return render(request,"addapp/addition.html")
   def post(self,request):    
      a = request.POST["txtnum1"]
      b = request.POST["txtnum2"]
      c = int(a)+int(b)
      return HttpResponse("Result is "+str(c))
   
class Prime(View):
    def get(self,request):
       return render(request,"addapp/prime.html")
    def post(self,request):    
        num = int(request.POST["txtnum"])
        s = ""
        for i in range(2,num):
            if num%i==0:
                s = "Not prime"
                break
        else:
             s = "prime"  
        return HttpResponse(s)           
class JobCreate(CreateView):
    model = Job
    fields = ['jobtitle', 'jobdescription']
    success_url = '/addapp/prime'
class JobList(ListView):
    model = Job    
