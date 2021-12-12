from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name = 'index'),
    path('select/', views.select, name = 'select'),
    path('result/', views.result, name = 'result'),
]