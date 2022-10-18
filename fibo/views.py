from django.shortcuts import render
def index(request):
    if request.method == "POST":
        n = int(request.POST['num'])
        if n > 0:
            a, b = 0, 1
            s = ''
            for i in range(n):
                s = s + str(a) + ', '
                c = a + b
                a = b
                b = c
            else:
                return HttpResponse(f'<h1>Fibonacci Series {n}:\n{s}</h1>')
        else:
            return HttpResponse('<h1>Number should be greater than 0</h1>')

    else:
        return render(request, 'fibo/fibo.html')


def new(request):
    if request.method == "POST":
        n = int(request.POST['num'])
        if n > 0:
            a, b = 0, 1
            s = ''
            for i in range(n):
                s = s + str(a) + ' '
                c = a + b
                a = b
                b = c
            else:
                return render(request, 'fibo/new.html', {'key':f'Fibonacci Series : {s}'})
        else:
            return render(request, 'fibo/new.html', {'key':'Error ! Number should be greater than 0'})

    else:
        return render(request, 'fibo/new.html')
# Create your views here.
