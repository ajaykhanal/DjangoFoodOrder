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


class Order(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    fname= models.CharField(max_length=150, null=False)
    lname= models.CharField(max_length=150, null=False)
    email= models.CharField(max_length=150, null=False)
    phone= models.CharField(max_length=150, null=False)
    city= models.CharField(max_length=150, null=False)
    address= models.TextField(max_length=150, null=False)
    total_price= models.FloatField(null=False)
    payment_mode= models.CharField(max_length=150, null=False)
    payment_id= models.CharField(max_length=250, null=False)
    orderstatuses= (
        ('Pending','Pending'),
        ('Out For Shipping','Out For Shipping'),
        ('Completed','Completed'),
    )
    status= models.CharField(max_length=150,choices=orderstatuses,default='Pending')
    tracking_no= models.CharField(max_length=150, null=True)
    created_at= models.DateTimeField(auto_now_add= True)
    updated_at= models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.user.username



class OrderItem(models.Model):
    order= models.ForeignKey(Order, on_delete=models.CASCADE)
    food= models.ForeignKey(Food, on_delete=models.CASCADE)
    price= models.FloatField(null=False)
    quantity= models.IntegerField(null=False)

    def __str__(self):
        return '{}'.format(self.order.id)

    









