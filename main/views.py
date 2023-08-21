from django.shortcuts import render
from .models import Partner, Department, Employee, Rectory, Service, Sahifalar
from fakultet.models import Chair, TeacherChair, Faculty, TeacherFaculty, New

def welcome(request):
    partners = Partner.objects.all() # hamkorlar
    faculties = Faculty.objects.all()
    news = New.objects.all()[:8]
    content = {
        'partners': partners,
        'faculties': faculties,
        'news': news
    }
    return render(request, 'main/welcome.html', content)

def gerb(request):
    content = {
        'faculties': Faculty.objects.all()
    }
    return render(request, 'main/ramzlar/gerb.html', content)

def bayroq(request):
    content = {
        'faculties': Faculty.objects.all()
    }
    return render(request, 'main/ramzlar/bayroq.html', content)

def madhiya(request):
    content = {
        'faculties': Faculty.objects.all()
    }
    return render(request, 'main/ramzlar/madhiya.html', content)

def vazifa(request):
    content = {
        'faculties': Faculty.objects.all()
    }
    return render(request, 'main/ramzlar/vazifa.html', content)

def rektorat(request):
    rectories = Rectory.objects.all()
    rector = None
    unrector = []
    for rectory in rectories:
        if rectory.is_rector:
            rector = rectory
        else:
            unrector.append(rectory)
    content = {
        'rector': rector,
        'rectories': unrector,
        'faculties': Faculty.objects.all()
    }
    return render(request, 'main/rektorat.html', content)


def qabul(request):

    content = {
        'faculties': Faculty.objects.all()
    }
    return render(request, 'main/qabulxona.html', content)

def store(request):  #chala
    pass

def xizmatlar(request):
    services = Service.objects.all()
    content = {
        'services': services,
        'faculties': Faculty.objects.all()
    }
    return render(request, 'main/xizmatlar.html', content)

def sahifalar(request, page):
    sahifa = Sahifalar.objects.get(page_name=page)
    content = {
        'sahifa': sahifa,
        'faculties': Faculty.objects.all(),
    }
    return render(request, 'main/page.html', content)

def markazlar(request):
    departments = Department.objects.all()
    content = {
        'departments': departments,
        'faculties': Faculty.objects.all()
    }
    return render(request, 'main/markazlar.html', content)

def markaz(request, pk):
    department = Department.objects.get(id=pk)
    employees = Employee.objects.filter(department=department)
    chief = None
    xodimlar = []
    for employee in employees:
        if employee.is_chief:
            chief = employee
        else:
            xodimlar.append(employee)
    content = {
        'department': department,
        'chief': chief,
        'employees': xodimlar,
        'faculties': Faculty.objects.all(),
    }
    return render(request, 'main/markaz.html', content)

def yangiliklar(request):
    news = New.objects.all()
    content = {
        'news': news,
        'faculties': Faculty.objects.all(),
    }
    return render(request, 'main/yangiliklar.html', content)

def yangilik(request, pk):
    new = New.objects.get(id=pk)
    news = New.objects.all()[:5]
    content ={
        'new': new,
        'news': news,
        'faculties': Faculty.objects.all(),
    }
    return render(request, 'main/yangilik.html', content)


def antikorrupsiya(request):
    content = {
        'faculties': Faculty.objects.all()
    }
    return render(request, 'main/korupsiya/korrupsiya.html', content)