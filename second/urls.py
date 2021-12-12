from django.urls import path
from . import views
# url_routing
urlpatterns = [
    path('list/', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('confirm/', views.confirm, name='confirm'),
]