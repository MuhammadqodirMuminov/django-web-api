from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()

class Reservation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)
    
    