from django.db import models
from django.contrib.auth.models import User
from .models import *

# Create your models here.


class Category(models.Model):
    title= models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.title


class Food(models.Model):
    name= models.CharField(max_length=50)
    description= models.CharField(max_length=200)
    price= models.IntegerField(default=0)
    category= models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    image= models.ImageField(upload_to='uploads/foods/')

    def __str__(self):
        return self.name




class Cart(models.Model):
    user= models.ForeignKey(User, on_delete= models.CASCADE)
    food= models.ForeignKey(Food, on_delete=models.CASCADE)
    food_qty= models.IntegerField(null=False, blank=False)
    created_at= models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.user.username

    









