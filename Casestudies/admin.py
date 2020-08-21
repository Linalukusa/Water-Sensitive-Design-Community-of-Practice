from django.contrib import admin
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

class CaseStudyAdmin (admin.ModelAdmin):
 list_display= ('title', 'paragraph_1','paragraph_2', 'paragraph_3', 'photo_1', )
 search_fields =('title',)

admin.site.register(casesoverview,CaseStudyAdmin )
admin.site.register(menlynn,CaseStudyAdmin )
admin.site.register(cotswolds, CaseStudyAdmin )
admin.site.register(capeTown,CaseStudyAdmin )
admin.site.register(rainbows, CaseStudyAdmin)
admin.site.register(Wits, CaseStudyAdmin)
admin.site.register(hawaans,CaseStudyAdmin )
admin.site.register(kzns,CaseStudyAdmin )
admin.site.register(pietermaritzburgs,CaseStudyAdmin )
admin.site.register(centurycitys,CaseStudyAdmin )
admin.site.register(RoofGarde, CaseStudyAdmin)
admin.site.register(verde,CaseStudyAdmin )
admin.site.register(report,CaseStudyAdmin )