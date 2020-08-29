from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Jasosel(models.Model):
    title = models.CharField(max_length=50)
    content=models.TextField()
    update_at=models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_posts')
    country=models.ForeignKey(Country,on_delete=models.SET_NULL,null=True)
    city=models.ForeignKey(City,on_delete=models.SET_NULL,null=True)

class Comment(models.Model):
    content = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    jasosel = models.ForeignKey(Jasosel, on_delete=models.CASCADE)

class Location(models.Model):
    location_name = models.CharField(max_length=50)
    sigungu = models.CharField(max_length=50)
    telephone=models.CharField(max_length=50)
    hashtag=models.CharField(max_length=150)