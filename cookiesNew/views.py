from django.shortcuts import render
from django.http import HttpResponse

def setcook(request):
    a = request.COOKIES['sk']
    if request.method == 'POST':
        txt2 = request.POST['cookieNew']
        setc = render(request, 'cookiesOld/index.html',{'keyold':txt2})
        setc.set_cookie('sk', txt2,max_age = None, expires = None)
        return setc
    return render(request, 'cookiesNew/index.html',{'keynew':a})
# Create your views here.
