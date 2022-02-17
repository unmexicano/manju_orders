from django.db import models
from datetime import datetime

# Create your models here.

class Category(models.Model):
    category_title = models.CharField(max_length=200)
    category_png = models.CharField(max_length=200)
    category_description = models.TextField(default='descripcion') #make this the wysiwyg text field

    def __str__(self):
        #overriding the string method to get a good representation of it in string format
        return f"{self.category_title}"

class opciones(models.Model):
    #example row :: 1 topping , 5.00 , 7.00
    relleno = models.CharField(max_length=200)
    small_price = models.DecimalField(max_digits=6, decimal_places=2)
    large_price = models.DecimalField(max_digits=6, decimal_places=2)
    category_description = models.TextField(default='descripcion manjus') #make this the wysiwyg text field

    def __str__(self):
        #overriding the string method to get a good representation of it in string format
        return f"sabor : {self.relleno}"


class UserOrder(models.Model):
    username = models.CharField(max_length=200) #who placed the order
    order = models.TextField() #this will be a string representation of the cart from localStorage
    price = models.DecimalField(max_digits=6, decimal_places=2) #how much was the order
    time_of_order  = models.DateTimeField(default=datetime.now, blank=True)
    delivered = models.BooleanField()

    def __str__(self):
        #overriding the string method to get a good representation of it in string format
        return f"Order placed by  : {self.username} on {self.time_of_order.date()} at {self.time_of_order.time().strftime('%H:%M:%S')}"

class SavedCarts(models.Model):
    username = models.CharField(max_length=200, primary_key=True)
    cart = models.TextField(default='descripcion') #this will be a string representation of the cart from localStorage

    def __str__(self):
        #overriding the string method to get a good representation of it in string format
        return f"Saved cart for {self.username}"
