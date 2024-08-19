from django.db import models
from CAFFOOD.models.customer import Customer


class Notification(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    head = models.CharField(max_length=20)
    message =  models.CharField(max_length=100)

    def __str__(self):
        return self.head

    @property
    def count_notifications(cls):
        return cls.objects.count()
