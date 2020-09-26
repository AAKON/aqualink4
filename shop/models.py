from django.db import models
from home.models import Product

# Create your models here.
class Shop(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self):
        return "%s ---> %s" %(self.product.name, self.price)

class oder_tb(models.Model):

    customer_name = models.CharField(max_length = 200)
    customer_address = models.CharField(max_length = 200)
    customer_phone = models.CharField(max_length = 200)
    customer_email = models.EmailField()

    def __str__(self):
        return self.customer_name

class Oder_item(models.Model):

    product_name = models.CharField(max_length = 200)
    product_id = models.IntegerField()
    product_quantity = models.IntegerField()
    oder_tb = models.ForeignKey(oder_tb, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name
