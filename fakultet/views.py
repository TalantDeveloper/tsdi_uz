from django.shortcuts import render, get_object_or_404, redirect
from .models import Chair, TeacherChair, New, Faculty, TeacherFaculty


def faculties_view(request):
    faculties = Faculty.objects.all()
    content = {
        'faculties': faculties,
    }
    return render(request, 'fakultet/fakultetlar.html', content)


def faculty_view(request, sub_name):
    faculty = Faculty.objects.get(sub_name=sub_name)
    faculties = Faculty.objects.all()
    chairs = faculty.kafedra.all()
    content = {
        'faculty': faculty,
        'faculties': faculties,
        'chairs': chairs,
    }
    return render(request, 'fakultet/fakultet.html', content)


def kafedralar_view(request):
    kafedralar = Chair.objects.all() # kafedralar
    content = {
        'kafedralar': kafedralar,
    }
    return render(request, 'kafedra/kafedralar.html', content)

def kafedra_view(request, sub_name):
    kafedra = Chair.objects.get(sub_name=sub_name)
    news = New.objects.filter(chair=kafedra)
    print(request.path_info)
    paths = request.path_info.strip('/').split('/')
    print(paths)

    content = {
        'kafedra': kafedra,
        'news': news
    }
    return render(request, 'kafedra/home/home.html', content)


def news_view(request):
    return render(request, 'kafedra/home/news.html')


def xodim(request):
    return render(request, 'kafedra/home/xodim.html')


def about(request):
    return render(request, 'kafedra/home/about.html')