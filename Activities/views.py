from django.shortcuts import render

# Create your views here.


def projects (request):
    
    return render (request, 'Activities/projects.html')
def training (request):
    return render (request, 'Activities/training.html')
def events (request):
    return render (request, 'Activities/events.html')

def output (request):
    return render (request, 'Activities/output.html')