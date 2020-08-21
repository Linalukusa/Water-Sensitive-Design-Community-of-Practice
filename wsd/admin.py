from django.contrib import admin
from .models import overview
from .models import cities
from .models import SustainableDrainage 
from .models import Modellings



admin.site.register(overview,  )

admin.site.register(cities, )
admin.site.register(SustainableDrainage , )
admin.site.register(Modellings, )