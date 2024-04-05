from django.db import models

# Create your models here.
class BrandModel(models.Model):
    Brand_Name = models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,unique=True)
    
    def __str__(self):
        return self.Brand_Name
