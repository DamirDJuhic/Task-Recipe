
from django.db import models
from django.db.models import Count
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
# Create your models here.
class Reception(models.Model):
   title = models.CharField(max_length=255)
   author = models.ForeignKey(User,on_delete=models.CASCADE)
   describe = models.TextField()
   reception_date = models.DateField(auto_now_add=True)
   
   def __str__(self):
      return self.title +'|'+ str(self.author)
   
   def get_absolute_url(self):
       return reverse('foodmaker',args=(str(self.id)))

RATING =(
   (1,'1'),
   (2,'2'),
   (3,'3'),
   (4,'4'),
   (5,'5'),
) 

class Rating(models.Model):
   reception = models.ForeignKey(Reception ,on_delete=models.CASCADE)
   user = models.ForeignKey(User,on_delete=models.CASCADE)
   rating = models.CharField(choices=RATING,max_length=150)
   create_date = models.DateTimeField(auto_now_add=True)
   updated_date = models.DateTimeField(auto_now_add=True)
   ip = models.CharField (max_length=20,blank=True)
   
class Writter (models.Model):
   first_name= models.OneToOneField(User ,on_delete=models.CASCADE, null=True,blank=True)
   last_name = models.CharField(max_length=200,null=True)
   email = models.EmailField('User Email')

   def __str__(self):
      return self.name
   
class Ingredient(models.Model):
   nameing = models.CharField(max_length=150)
   recipe = models.ForeignKey(Reception,on_delete=models.CASCADE,related_name="ingredients" )
   ingredient = models.ManyToManyField(Reception)
   
   def __str__(self):
      return self.name