from django.db import models
from brand.models import BrandModel
from django.contrib.auth.models import User
# Create your models here.
class Car_Model(models.Model):
    file=models.ImageField(upload_to='uploads/')
    car_name=models.CharField(max_length=100)
    description=models.TextField()
    price=models.IntegerField()
    quantity=models.IntegerField(null=True,blank=True,)
    brand=models.ForeignKey(BrandModel,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.car_name


class Comment(models.Model):
    car_model=models.ForeignKey(Car_Model,on_delete=models.CASCADE, related_name='comments')
    name=models.CharField(max_length=100)
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    car_model=models.ForeignKey(Car_Model,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    
    def total_price(self):
        return self.quantity * self.car_model.price
    
    def __str__(self):
        return self.user.username
