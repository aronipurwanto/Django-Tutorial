from django.db import models
from django.contrib.auth.models import AbstractUser

class Category(models.Model):
    code = models.CharField(max_length=20, default='C001')
    name = models.CharField(max_length=255)

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    description = models.TextField(blank=True)  # Deskripsi produk (opsional)

class Customer(models.Model):
    name = models.CharField(max_length=255)
    member = models.BooleanField(default=False)  # Apakah pelanggan member?

class Transaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)  # Pelanggan (opsional)
    products = models.ManyToManyField(Product, through='TransactionItem')  # Produk-produk dalam transaksi
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)

class TransactionItem(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()