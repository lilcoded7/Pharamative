from setup.basemodel import TimeBaseModel
from CAFFOOD.models.food import Food
from CAFFOOD.models.order import Order 
from django.db import models 


class OrderItem(TimeBaseModel):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    order    = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    def item_status(self):
        self.status='paid'
        self.save()

    @property
    def get_total(self):
        total = self.food.price * self.quantity 
        return total 

    def __str__(self):
        return str(self.id) 