from django.db import models 
from django.contrib.auth import get_user_model

User = get_user_model()


class UsedCode(models.Model):
    code = models.CharField(max_length=100, null=True, blank=True) 

    def __str__(self):
        return self.code 
