from django.shortcuts import render
from django.http import HttpResponse
from .models import About




def about (request):
    pages = About.objects.all()
    context = {
        'pages': pages
    }
    return render (request, 'pages/about.html',context )











  