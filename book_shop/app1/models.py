from django.db import models

# Create your models here.
from django.db.models import FloatField


class Book(models.Model):
    # title price author full_text file
    title = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField(max_length=1000)

    def __str__(self):
        return '{} {} $'.format(self.title, self.price)


class GuitarAkk(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    color = models.CharField(max_length=20, blank=True, null=True, default='')
    description = models.TextField(max_length=1000)
    img = models.ImageField(upload_to='img_guitar/', blank=True, null=True, default='')

    def __str__(self):
        return '{} {} $'.format(self.title, self.price)


class GuitarEl(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    color = models.CharField(max_length=20)
    description = models.TextField(max_length=1000, null=True, blank=True, default='')
    img = models.ImageField(upload_to='img_elguitar/', blank=True, null=True, default='')

    def __str__(self):
        return '{} {} $'.format(self.title, self.price)


class Equipments(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    color = models.CharField(max_length=20)
    description = models.TextField(max_length=1000, null=True, blank=True, default='')
    img = models.ImageField(upload_to='img_equipments/', blank=True, null=True, default='')

    def __str__(self):
        return '{} {} $'.format(self.title, self.price)


class Key(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    color = models.CharField(max_length=20)
    description = models.TextField(max_length=1000, null=True, blank=True, default='')
    img = models.ImageField(upload_to='img_keys/', blank=True, null=True, default='')

    def __str__(self):
        return '{} {} $'.format(self.title, self.price)