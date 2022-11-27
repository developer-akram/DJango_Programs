from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class Addition(View):
    def get(self, request):
        return render(request, 'classView/index.html')
    def post(self, request):
        a = request.POST['num1']
        b = request.POST['num2']
        c = int(a) + int(b)
        return render(request, 'classView/index.html',{'ans':c})

# Create your views here.
