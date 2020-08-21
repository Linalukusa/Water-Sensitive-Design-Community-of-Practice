from django.contrib import admin
from .models import About

class AboutAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'paragraph_1', 'photo_1', 'photo_2', 'paragraph_2', 'paragraph_3', 'paragraph_4', 'paragraph_5', 'paragraph_6' )
    list_display_links = ('id', 'title')

admin.site.register(About, AboutAdmin)
