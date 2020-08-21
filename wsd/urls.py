from django.urls import path
from . import views
urlpatterns = [
   
    path('wsdoverview', views.wsdoverview, name='wsdoverview'),
    path('watersensitivecities', views.watersensitivecities, name='watersensitivecities'),
    path('drainagesystems', views.drainagesystems, name='drainagesystems'),
    path('wsdsa', views.wsdsa, name='wsdsa'),
    path('modelling', views.modelling, name='modelling'),

    
    
]