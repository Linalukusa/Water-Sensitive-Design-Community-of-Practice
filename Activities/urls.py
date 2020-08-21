from django.urls import path
from . import views
urlpatterns = [
   
    path('projects', views.projects, name='projects'),
    path('training', views.training, name='training'),
    path('events', views.events, name='events'),
    path('output', views.output, name='output'),


]