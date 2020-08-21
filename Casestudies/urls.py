from django.urls import path
from . import views
urlpatterns = [
   
    path('casestudiesoverview', views.casestudiesoverview, name='casestudiesoverview'),
    path('menlyn', views.menlyn, name='menlyn'),
    path('cotswold', views.cotswold, name='cotswold'),
    path('capetown', views.capetown, name='capetown'),
    path('rainbow', views.rainbow, name='rainbow'),
    path('wits', views.wits, name='wits'),
    path('hawaan', views.hawaan, name='hawaan'),
    path('kzn', views.kzn, name='kzn'),
    path('pietermaritzburg', views.pietermaritzburg, name='pietermaritzburg'),
    path('centurycity', views.centurycity, name='centurycity'),
    path('roofgarden', views.roofgarden, name='roofgarden'),
    path('hotelverde', views.hotelverde, name='hotelverde'),
    path('reports', views.reports, name='reports'),
    path('projectwilliam', views.projectwilliam, name='projectwilliam'),
    path('projectdavid', views.projectdavid, name='projectdavid'),





] 