
 
from django.db import models

class About (models.Model):
    title = models.CharField(max_length=500)
    paragraph_1 = models.TextField(blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    paragraph_2 = models.TextField(blank=True)
    paragraph_3 = models.TextField(blank=True)
    paragraph_4 = models.TextField(blank=True)
    paragraph_5 = models.TextField(blank=True)
    paragraph_6 = models.TextField(blank=True)

def __str__(self):
    return self.title
