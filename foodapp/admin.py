from django.contrib import admin
from .models import Food
from .models import Category
from .models import Cart
from .models import Order
from .models import OrderItem

# Register your models here.

class AdminFood(admin.ModelAdmin):
    list_display= ['name','price','category']


class AdminCategory(admin.ModelAdmin):
    list_display= ['title']

class AdminCart(admin.ModelAdmin):
    list_display= ['user','food','food_qty']

class AdminOrder(admin.ModelAdmin):
    list_display= ['fname','lname','total_price']

class AdminOrderItem(admin.ModelAdmin):
    list_display= ['order','food','price']

admin.site.register(Food,AdminFood)
admin.site.register(Category,AdminCategory)
admin.site.register(Cart,AdminCart)
admin.site.register(Order,AdminOrder)
admin.site.register(OrderItem,AdminOrderItem)
