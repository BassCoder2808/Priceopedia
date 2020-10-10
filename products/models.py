from django.db import models
from users.models import Category
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    product_id = models.CharField(max_length=15,primary_key=True)
    product_name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=0)
    rating = models.DecimalField(max_digits=5,decimal_places=2)
    number_of_users_bought = models.IntegerField()
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

class History(models.Model):
    product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    curr_price = models.DecimalField(max_digits=10,decimal_places=0)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.curr_price} for {self.product_id.product_name} for date {self.date}."
