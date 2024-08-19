from setup.basemodel import TimeBaseModel
from django.contrib.auth import get_user_model
from django.db import models 

User = get_user_model()


class Customer(TimeBaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name 