from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if request.method == "POST":
        a = int(request.POST['num'])
        if a > 0:
            f = 1
            for i in range (a,0,-1):
                f = f * i
            else:
                return HttpResponse(f"<h1>{a}! = {f}</h1>")
        else:
            return HttpResponse('Number should be greater than 0')
    else:
        return render(request, 'fact/fact.html')
def new(request):
    if request.method == "POST":
        a = int(request.POST['num'])
        if a > 0:
            f = 1
            for i in range(a, 0, -1):
                f = f * i
            else:
                value = f"{a}! = {f}"
                return render(request, 'fact/new.html',{'key':value})
        else:
            return render(request, 'fact/new.html',{'key':'Number should be greater than 0'})
    else:
        return render(request, 'fact/new.html')

# Create your views here.
