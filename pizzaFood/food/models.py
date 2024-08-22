
from django.db import models

# Modèle pour les types de pizza
class Pizza(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='pizzas', blank= True, null= True)  # nécessite Pillow

    def __str__(self):
        return self.name

# Modèle pour une commande
class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_address = models.TextField()
    customer_phone = models.CharField(max_length=15)
    ordered_pizzas = models.ManyToManyField(Pizza, through="OrderItem")
    total_price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.customer_name}"

# Modèle pour les articles dans la commande
class OrderItem(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.pizza.name}"
