

from django.db import models
from django.urls import reverse

# Create your models here.

class Index_start(models.Model):
    name1 = models.CharField(max_length=200)
    name2 = models.CharField(max_length=200)
    name3 = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    def get_absolute_url(self):
        return reverse("detail1", args=[self.slug])
    def __str__(self):
        return self.name1
    


class About(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    skil = models.CharField(max_length=200) 
    skil_bio = models.TextField()
    img = models.ImageField(upload_to='about/')
    def __str__(self):
        return self.name

class Birthday(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='birthday_cake/')
    slug = models.SlugField(max_length=200)
    def get_absolute_url(self):
        return reverse("detail2", args=[self.slug])  
    def __str__(self):
        return self.name

class Wedding(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='wedding_cake/')
    slug = models.SlugField(max_length=200)
    def get_absolute_url(self):
        return reverse("detail3", args=[self.slug])
    def __str__(self):
        return self.name

class Custom(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='custom_cake/')
    slug = models.SlugField(max_length=200)
    def get_absolute_url(self):
        return reverse('detail4', args=[self.slug])
    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    slug = models.SlugField(max_length=200)
    def get_absolute_url(self):
        return reverse("detail5", args=[self.slug])
    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    img = models.ImageField(upload_to='team/')
    slug = models.SlugField(max_length=200)
    def get_absolute_url(self):
        return reverse("detail6", args=[self.slug])
    def __str__(self):
        return self.name

class Offer(models.Model):
    name1 = models.CharField(max_length=200)
    name2 = models.CharField(max_length=200)
    bio = models.TextField()
    slug = models.SlugField(max_length=200)
    def get_absolute_url(self):
        return reverse("detail7", args=[self.slug])
    def __str__(self):
        return self.name1
    
class Client(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    profession = models.CharField(max_length=200)
    img = models.ImageField(upload_to='client/')
    slug = models.SlugField(max_length=200)
    def get_absolute_url(self):
        return reverse("detail8", args=[self.slug])
    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    def __str__(self):
        return self.name  