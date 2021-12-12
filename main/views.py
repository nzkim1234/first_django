from django.shortcuts import render
from django.template import loader
# Create your views here.

def list(request):
    context = {

    }
    return render(request, 'main/base.html', context)