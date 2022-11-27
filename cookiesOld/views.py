from django.shortcuts import render
from django .http import HttpResponse

def getcook(request):
    a = request.COOKIES['sk']
    if request.method == 'POST':
        text = request.POST['cookieOld']
        setc = render(request, 'cookiesNew/index.html',{'keynew':text})
        setc.set_cookie('sk', text, max_age = None, expires = None)
        return setc
    return render(request, 'cookiesOld/index.html', {'keyold':a})
# Create your views here.
