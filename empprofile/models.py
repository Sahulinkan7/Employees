from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=40)
    email=models.EmailField()
    phone=models.CharField(max_length=12,blank=True)
    image=models.ImageField(upload_to="images")
    
    def __str__(self) -> str:
        return self.first_name
