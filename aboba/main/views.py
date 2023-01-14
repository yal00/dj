from django.shortcuts import render

# Create your views here.
def index(request):
    data = {
        'title': 'Главная страница',
    }
    return render(request, 'main/home.html', data)

def about(request):
    data = {
        'title': 'Востребованность',
    }
    return render(request, 'main/demand.html', data)

def geography(request):
    data = {
        'title': 'Георгафия',
    }
    return render(request, 'main/geography.html', data)

def skills(request):
    data = {
        'title': 'Навыки',
    }
    return render(request, 'main/skills.html', data)

def vacancy(request):
    data = {
        'title': 'Последние вакансии',
    }
    return render(request, 'main/vacancy.html', data)
