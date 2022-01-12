from django.db import models
from authentication.models import User


def upload_products(instance, filename):

    filename = filename.split(".")
    ext = filename.pop()
    filename = "".join(filename)+ "." + ext
    return f"Product_Images/{filename}"



class Category(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Brand(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Detail(models.Model):

    front = models.ImageField(upload_to=upload_products, null=True)
    back = models.ImageField(upload_to=upload_products, null=True)
    left = models.ImageField(upload_to=upload_products, null=True)
    right = models.ImageField(upload_to=upload_products, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.description}"


class Product(models.Model):

    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    weight = models.FloatField(default=0)
    color = models.CharField(max_length=255)
    detail = models.OneToOneField(Detail, on_delete=models.CASCADE)
    is_sold = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


