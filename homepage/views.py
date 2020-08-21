from django.shortcuts import render
from django.http import HttpResponse
from .models import Homepages

# Create your views here.

def index (request):
    homepage = Homepages.objects.all()
    context = {
        'homepage': homepage
    }
    return render (request, 'homepage/index.html', context)
