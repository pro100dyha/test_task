from django.db import models


class Order(models.Model):
    number = models.IntegerField()
    created_date = models.DateTimeField()


class OrderItem(models.Model):
    order = models.ForeignKey(
        'orders.Order',
        related_name='items',
        on_delete=models.CASCADE
    )
    product_name = models.CharField(max_length=127)
    product_price = models.DecimalField(max_digits=6,  decimal_places=2)
    amount = models.IntegerField()
