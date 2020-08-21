
from django.db import models

class overview (models.Model):
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

class cities (models.Model):
    title = models.CharField(max_length=1000)
    paragraph_1 = models.TextField(blank=True)
    paragraph_2 = models.TextField(blank=True)
    paragraph_3 = models.TextField(blank=True)
    paragraph_4 = models.TextField(blank=True)
    paragraph_5 = models.TextField(blank=True)
    paragraph_6 = models.TextField(blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    paragraph_7 = models.TextField(blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

def __str__(self):
    return self.title


class SustainableDrainage (models.Model):
    title = models.CharField(max_length=1000)
    paragraph_1 = models.TextField(blank=True)

def __str__(self):
    return self.title


class Modellings (models.Model):
    title = models.CharField(max_length=1000)
    paragraph_1 = models.TextField(blank=True)
    paragraph_2 = models.TextField(blank=True)
    paragraph_3 = models.TextField(blank=True)
    paragraph_4 = models.TextField(blank=True)
    paragraph_5 = models.TextField(blank=True)
    paragraph_6 = models.TextField(blank=True)
    paragraph_7 = models.TextField(blank=True)
    paragraph_8 = models.TextField(blank=True)
    paragraph_9 = models.TextField(blank=True)
    paragraph_10 = models.TextField(blank=True)
    paragraph_11 = models.TextField(blank=True)
    paragraph_12 = models.TextField(blank=True)
    paragraph_13 = models.TextField(blank=True)
    paragraph_14 = models.TextField(blank=True)
    paragraph_15 = models.TextField(blank=True)
    paragraph_16 = models.TextField(blank=True)
    paragraph_17 = models.TextField(blank=True)
    paragraph_18 = models.TextField(blank=True)
    paragraph_19 = models.TextField(blank=True)
    paragraph_20 = models.TextField(blank=True)
    paragraph_21 = models.TextField(blank=True)
    paragraph_22 = models.TextField(blank=True)
    paragraph_23 = models.TextField(blank=True)
    paragraph_24 = models.TextField(blank=True)
    paragraph_25 = models.TextField(blank=True)
    paragraph_26 = models.TextField(blank=True)
    paragraph_27 = models.TextField(blank=True)
    paragraph_28 = models.TextField(blank=True)
    paragraph_28 = models.TextField(blank=True)


def __str__(self):
    return self.title

class wsdSA (models.Model):
    title = models.CharField(max_length=1000)
    paragraph_1 = models.TextField(blank=True)
    paragraph_2 = models.TextField(blank=True)
    paragraph_3 = models.TextField(blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)


def __str__(self):
    return self.title


