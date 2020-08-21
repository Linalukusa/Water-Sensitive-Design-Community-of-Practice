
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include ('pages.urls')),
    path('admin/', admin.site.urls),
    path('', include ('homepage.urls')),
    path('', include ('Activities.urls')),
    path('', include ('Casestudies.urls')),
    path('', include ('contact.urls')),
    path('', include ('resources.urls')),
    path('', include ('wsd.urls')),


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
