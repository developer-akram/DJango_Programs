from django.shortcuts import render

def index(request):
    if request.method == "POST":
        name = request.POST['name']
        s1 = int(request.POST['sub1'])
        s2 = int(request.POST['sub2'])
        s3 = int(request.POST['sub3'])
        s4 = int(request.POST['sub4'])
        s5 = int(request.POST['sub5'])
        if 0 <= s1 <= 100 and  0 <= s2 <= 100 and  0 <= s3 <= 100 and  0 <= s4 <= 100 and  0 <= s5 <= 100:
            c = 0
            s = ''
            d = ''
            if s1 <33:
                c += 1
                g = s1
                s += " Sub1"
            if s2 <33:
                c += 1
                g = s2
                s += " Sub2"
            if s3 <33:
                c += 1
                g = s3
                s += " Sub3"
            if s4 <33:
                c += 1
                g = s4
                s += " Sub4"
            if s5 <33:
                c += 1
                g = s5
                s += " Sub5"
            if s1 >= 90:
                d += " Sub1"
            if s2 >= 90:
                d += " Sub2"
            if s3 >= 90:
                d += " Sub3"
            if s4 >= 90:
                d += " Sub4"
            if s5 >= 90:
                d += " Sub5"
            if len(d) != 0:
                ds = f'<br>Distinction in {d}'
            else:
                ds = ''
            if c == 0 or c == 1 and g >= 28:
                per = ( s1 + s2 + s3 + s4 + s5 ) / 5
                txt = ''
                if c == 1:
                    per += (33-g) / 5
                    txt = f" by Grace<br>Grace in : {s}<br>Got grace mark : {33-g}"
                if per < 45:
                    grade = '<br>Grade : D<br>'
                elif per < 50:
                    grade = '<br>Grade : C<br>'
                elif per < 60:
                    grade = '<br>Grade : B<br>'
                elif per >= 60:
                    grade = '<br>Grade : A<br>'
                return HttpResponse(f"<h1>Name : {name}<br>Pass{txt}{grade}Percentage = {per:.2f}{ds}</h1>")
            elif c == 1:
                return HttpResponse(f"<h1>Name : {name}<br>Supplymentry in {s}{ds}</h1>")
            else:
                return HttpResponse(f"<h1>Name : {name}<br>Fail in {s}{ds}</h1>")
        return HttpResponse("<h1>Each Subjects marks should be 0 to 100</h1>")
    else:
        return render(request, 'marksheet/new.html')
def new(request):
    if request.method == "POST":
        text = {'Error ! ': 'Each Subjects marks should be 0 to 100'}
        name = request.POST['name']
        s1 = int(request.POST['sub1'])
        s2 = int(request.POST['sub2'])
        s3 = int(request.POST['sub3'])
        s4 = int(request.POST['sub4'])
        s5 = int(request.POST['sub5'])
        if 0 <= s1 <= 100 and 0 <= s2 <= 100 and 0 <= s3 <= 100 and 0 <= s4 <= 100 and 0 <= s5 <= 100:
            text.clear()
            text.update({'Name : ':name})
            c = 0
            s = ''
            d = ''
            if s1 < 33:
                c += 1
                g = s1
                s += " Sub1"
            if s2 < 33:
                c += 1
                g = s2
                s += " Sub2"
            if s3 < 33:
                c += 1
                g = s3
                s += " Sub3"
            if s4 < 33:
                c += 1
                g = s4
                s += " Sub4"
            if s5 < 33:
                c += 1
                g = s5
                s += " Sub5"
            if s1 >= 90:
                d += " Sub1"
            if s2 >= 90:
                d += " Sub2"
            if s3 >= 90:
                d += " Sub3"
            if s4 >= 90:
                d += " Sub4"
            if s5 >= 90:
                d += " Sub5"
            if len(d) != 0:
                text.update({'Distinction in : ': d})
            if c == 0 or c == 1 and g >= 28:
                per = (s1 + s2 + s3 + s4 + s5) / 5
                txt = ''
                if c == 1:
                    per += (33 - g) / 5
                    txt = f" by Grace"
                    text.update({'Grace in : ':s})
                    text.update({'Got grace mark : ':33 - g})
                text.update({'Result : ': 'Pass' + txt})
                text.update({'Percentage : ': f"{per:.2f}"+' %'})
                if per < 45:
                    grade = 'D'
                elif per < 50:
                    grade = 'C'
                elif per < 60:
                    grade = 'B'
                elif per >= 60:
                    grade = 'A'
                text.update({'Grade : ':grade})
                return render(request, 'marksheet/new.html', {'key':text})
            elif c == 1:
                text.update({'Supplymentry in :':s})
                return render(request, 'marksheet/new.html', {'key':text})
            else:
                text.update({'Fail in':s})
                return render(request, 'marksheet/new.html', {'key':text})
        return render(request, 'marksheet/new.html', {'key':text})
    else:
        return render(request, 'marksheet/new.html')
# Create your views here.
