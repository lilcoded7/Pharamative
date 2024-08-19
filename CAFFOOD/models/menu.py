from django.db import models 
from setup.basemodel import TimeBaseModel



class Menu(TimeBaseModel):
    name = models.CharField(max_length=100)

    def __str__(self)-> str:
        return str(self.name)