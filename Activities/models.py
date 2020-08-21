
from django.db import models

class trainings (models.Model):
    title = models.CharField(max_length=1000)
    paragraph_1 = models.TextField(blank=True)
    paragraph_2 = models.TextField(blank=True)
    paragraph_3 = models.TextField(blank=True)
    paragraph_4 = models.TextField(blank=True)
    paragraph_5 = models.TextField(blank=True)
    paragraph_6 = models.TextField(blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    paragraph_7 = models.TextField(blank=True)


def __str__(self):
    return self.title

class projects (models.Model):
    title = models.CharField(max_length=1000)
    paragraph_1 = models.TextField(blank=True)
    paragraph_2 = models.TextField(blank=True)
    paragraph_3 = models.TextField(blank=True)
    paragraph_4 = models.TextField(blank=True)
    paragraph_5 = models.TextField(blank=True)
    paragraph_6 = models.TextField(blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    paragraph_7 = models.TextField(blank=True)


def __str__(self):
    return self.title


class outputs (models.Model):
    title = models.CharField(max_length=1000)
    paragraph_1 = models.TextField(blank=True)

def __str__(self):
    return self.title


class event (models.Model):
    title = models.CharField(max_length=1000)
    paragraph_1 = models.TextField(blank=True)
    paragraph_2 = models.TextField(blank=True)
    paragraph_3 = models.TextField(blank=True)
    paragraph_4 = models.TextField(blank=True)
    paragraph_5 = models.TextField(blank=True)
    paragraph_6 = models.TextField(blank=True)
    

def __str__(self):
    return self.title

