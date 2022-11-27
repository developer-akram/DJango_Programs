from django.shortcuts import render
from autocrud.models import *
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class EmpCreate(CreateView):
    model = Worker
    fields = ['name','gender','mobile','email']
    success_url = '/autocrud/emplist'

class EmpList(ListView):
    model = Worker

class EmpDelete(DeleteView):
    model = Worker
    success_url = '/autocrud/emplist'

class EmpDetail(DetailView):
    model = Worker

class EmpUpdate(UpdateView):
    model = Worker
    fields = ['name','gender','mobile','email']
    success_url = '/autocrud/emplist'

# Create your views here.
