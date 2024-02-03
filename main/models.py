from django.db import models


class Order(models.Model):
    class Status(models.TextChoices):
        CREATED = "CREATED"
        PENDING = "PENDING"
        PAID = "PAID"
        CANCELED = "CANCELED"

    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    product_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.CREATED)
    def __str__(self):
        return self.full_name
