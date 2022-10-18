from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    a = 100
    b = 20
    return HttpResponse(f"{a} - {b} = {a-b}")


def u_input(request):
    if request.method == "POST":
        a = int(request.POST['num1'])
        b = int(request.POST['num2'])
        c = a - b
        return HttpResponse("Result = " + str(c))
    else:
        return render(request, 'sub/sub.html')