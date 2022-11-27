from django.shortcuts import render
from django.http import HttpResponse
from allclassview.models import Job
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# from django.urls import reverse

class JobCreate(CreateView):
    model = Job
    fields = ['jobtitle','jobdescription']
    success_url = '/allclassview/joblist'

class JobList(ListView):
    model = Job

class JobDetail(DetailView):
    model = Job 

class JobUpdate(UpdateView):
    model = Job
    fields = ['jobtitle', 'jobdescription']
    success_url = '/allclassview/joblist'

class JobDelete(DeleteView):
    model = Job
    success_url = '/allclassview/joblist'
    

# Create your views here.
