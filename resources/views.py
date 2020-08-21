from django.shortcuts import render

# Create your views here.
def guidelines (request):
    return render (request, 'resources/guidelines.html')

def wsdexpertise (request):
    return render (request, 'resources/wsdexpertise.html')
    
def internationalmanual (request):
    return render (request, 'resources/internationalmanual.html')

def websites (request):
    return render (request, 'resources/websites.html')