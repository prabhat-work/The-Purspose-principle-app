from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name= models.CharField(max_length = 200, default='abc') 
    title = models.CharField(max_length = 200)
    body = models.CharField(max_length = 200 , default='SOME STRING')
    url = models.CharField(max_length = 120,default='STRING')
    summary = models.CharField(max_length = 125, default="string2")
    # body = models.CharField(max_length=1000)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)
    
def __str__(self):
    return self.title 

def __str__(self):
    return self.body     





