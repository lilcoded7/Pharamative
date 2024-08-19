from django.contrib import admin
from CAFFOOD.models.customer import Customer
from CAFFOOD.models.food import Food
from CAFFOOD.models.category import Category
from CAFFOOD.models.order import Order
from CAFFOOD.models.order_item import OrderItem
from CAFFOOD.models.menu import Menu
from CAFFOOD.models.notification import Notification
# Register your models here.

class FoodAdmin(admin.ModelAdmin):
    list_display = ['name']

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['quantity']


admin.site.register(Food, FoodAdmin)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Menu)
admin.site.register(Customer)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Notification)