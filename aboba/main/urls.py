from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Главная страница'),
    path('demand/', views.about, name='Востребованность'),
    path('geography/', views.geography, name='География'),
    path('skills/', views.skills, name='Навыки'),
    path('vacancy/', views.vacancy, name='Последние вакансии'),
]