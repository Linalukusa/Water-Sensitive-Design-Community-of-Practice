from django.shortcuts import render
from .models import overview
from .models import cities
from .models import SustainableDrainage
from .models import Modellings
from .models import wsdSA 



def wsdoverview (request):
    wsd = overview.objects.all()
    context = {
        'wsd': wsd
    }
    return render (request, 'wsd/wsdoverview.html',context )

  
def watersensitivecities (request):
    wsd = cities.objects.all()
    context = {
        'wsd': wsd
    }
    return render (request, 'wsd/watersensitivecities.html', context)


def drainagesystems (request):
    wsd = SustainableDrainage.objects.all()
    context = {
        'wsd': wsd
    }
    return render (request, 'wsd/drainagesystems.html', context)

def wsdsa (request):
    wsd = wsdSA.objects.all()
    context = {
        'wsd': wsd
    }
    return render (request, 'wsd/wsdsa.html', context)

def modelling (request):
    wsd = Modellings.objects.all()
    context = {
        'wsd': wsd
    }
    return render (request, 'wsd/modelling.html', context)