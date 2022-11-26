from django.db import models
from django.utils import timezone


class Inventory(models.Model):
    product_name = models.CharField(max_length=100, null=False, blank=False)
    cost_per_item = models.DecimalField(max_digits=19, decimal_places=2, null=False, blank=False)
    quantity_in_stock = models.IntegerField(null=False, blank=False)
    quantity_sold = models.IntegerField(null=False, blank=True)
    sales = models.DecimalField(max_digits=19, decimal_places=2, null=False, blank=False)
    stock_date = models.DateField(default=timezone.now)
    last_sales_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.product_name

class  Sale(models.Model):
    point_received = models.IntegerField(default=1)
    discount = models.DecimalField(max_digits=19, decimal_places=2, null=False, blank=False)
    name = models.ForeignKey(Inventory, on_delete=models.CASCADE, null=False, blank=False)
    total_sale = models.DecimalField(max_digits=19, decimal_places=2, null=False, blank=False)

    