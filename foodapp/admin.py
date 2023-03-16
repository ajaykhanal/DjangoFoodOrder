from django.contrib import admin
from .models import Food
from .models import Category
from .models import Cart

# Register your models here.

class AdminFood(admin.ModelAdmin):
    list_display= ['name','price','category']


class AdminCategory(admin.ModelAdmin):
    list_display= ['title']

class AdminCart(admin.ModelAdmin):
    list_display= ['user','food','food_qty']

admin.site.register(Food,AdminFood)
admin.site.register(Category,AdminCategory)
admin.site.register(Cart,AdminCart)
