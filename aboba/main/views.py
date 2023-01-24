from django.shortcuts import render
from .models import Homeblocks, Demand, Geo, Topskills
from .get_hh import main

def index(request):
    title = 'Главная страница'
    data = Homeblocks.objects.all()
    return render(request, 'main/home.html', {'data': data, 'title': title})

def about(request):
    title = 'Востребованность'
    data = Demand.objects.all()
    return render(request, 'main/demand.html', {'title': title, 'data': data})

def geography(request):
    title = 'Георгафия'
    data = Geo.objects.all()
    return render(request, 'main/geography.html', {'title': title, 'data': data})

def skills(request):
    title = 'Навыки'
    data = Topskills.objects.all()
    return render(request, 'main/skills.html', {'title': title, 'data': data})

def vacancy(request):
    data = main()
    title = 'Последние вакансии'
    return render(request, 'main/vacancy.html', {'title': title, 'data': data})
