from django.urls import path
from . import views
urlpatterns = [
   

    path('guidelines', views.guidelines, name='guidelines'),
    path('wsdexpertise', views.wsdexpertise, name='wsdexpertise'),
    path('internationalmanual', views.internationalmanual, name='internationalmanual'),
    path('websites', views.websites, name='websites'),

    
]