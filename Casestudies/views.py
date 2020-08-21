from django.shortcuts import render
from .models import casesoverview
from .models import menlynn
from .models import cotswolds
from .models import capeTown
from .models import rainbows
from .models import Wits
from .models import hawaans
from .models import kzns
from .models import pietermaritzburgs
from .models import centurycitys
from .models import RoofGarde
from .models import verde
from .models import report


# Create your views here.



def casestudiesoverview (request):
    Casestudies = casesoverview.objects.all()
    context = {
        'Casestudies': Casestudies
    }
    return render (request, 'Casestudies/casestudiesoverview.html', context)
    
def menlyn (request):
    Casestudies = menlynn.objects.all()
    context = {
        'Casestudies': Casestudies
    }
    return render (request, 'Casestudies/menlyn.html', context)

def cotswold (request):
    Casestudies = cotswolds.objects.all()
    context = {
        'casestudies': Casestudies
    }
    return render (request, 'Casestudies/cotswold.html', context)


def capetown (request):
    Casestudies = capeTown.objects.all()
    context = {
        'Casestudies': Casestudies
    }
    return render (request, 'Casestudies/capetown.html', context)

def rainbow (request):
    Casestudies = rainbows.objects.all()
    context = {
        'Casestudies': Casestudies
    }
    return render (request, 'Casestudies/rainbow.html', context)

def wits (request):
    Casestudies = Wits.objects.all()
    context = {
        'Casestudies': Casestudies
    }
    return render (request, 'Casestudies/wits.html', context)

def hawaan (request):
    Casestudies = hawaans.objects.all()
    context = {
        'Casestudies': Casestudies
    }
    return render (request, 'Casestudies/hawaan.html', context)

def kzn (request):
    Casestudies = kzns.objects.all()
    context = {
        'casestudies': Casestudies
    }
    return render (request, 'Casestudies/kzn.html', context)

def pietermaritzburg (request):
    Casestudies = pietermaritzburgs.objects.all()
    context = {
        'Casestudies': Casestudies
    }
    return render (request, 'Casestudies/pietermaritzburg.html', context)

def centurycity (request):
    Casestudies = centurycitys.objects.all()
    context = {
        'Casestudies': Casestudies
    }
    return render (request, 'Casestudies/centurycity.html', context)

def roofgarden (request):
    Casestudies = RoofGarde.objects.all()
    context = {
        'Casestudies': Casestudies
    }
    return render (request, 'Casestudies/roofgarden.html', context)
def hotelverde (request):
    Casestudies = verde.objects.all()
    context = {
        'Casestudies': Casestudies
    }
    return render (request, 'Casestudies/hotelverde.html', context)


def reports (request):
    Casestudies = report.objects.all()
    context = {
        'Casestudies': Casestudies
    }
    return render (request, 'Casestudies/reports.html', context)

def projectdavid (request):
    return render (request, 'Casestudies/projectdavid.html', )

def projectwilliam (request):
    return render (request, 'Casestudies/projectwilliam.html', )





