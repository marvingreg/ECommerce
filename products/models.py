from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    customer = models.OneToOneField(User,on_delete=models.CASCADE)
    