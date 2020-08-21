
from django.db import models

class   Homepages (models.Model):
    title = models.CharField(max_length=500)
    sub_title = models.CharField(max_length=500)
    paragraph_1 = models.TextField(blank=True)
    paragraph_2 = models.TextField(blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)


def __str__(self):
    return self.title
