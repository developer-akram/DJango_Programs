from django.shortcuts import redirect, render
from django.http import HttpResponse
from cookies.models import *  
def setcookie(request):
    # data = HttpResponse('Cookie has been SET')
    # data.set_cookie('ckey',"My Value", max_age=180)
    # return data
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        mobile = request.POST['mobile']
        data = Employee(username = username, password = password, email = email, mobile = mobile)
        data.save()
        return redirect('/cookies/login')
    return render(request, 'cookies/index.html')

def getcookie(request):
    show = request.COOKIES['ckey']
    return HttpResponse(f'Value is : {show}')

def login(request):
    return render(request, 'cookies/login.html')


# Create your views here.
