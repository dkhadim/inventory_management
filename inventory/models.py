from django.db import models

# =======================
# ==== CATEGORIES =======
# =======================

class Categories(models.Model):
    name = models.CharField(max_length=300)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)

# =======================   
# ==== SUPPLIERS ========
# =======================    
    
class Suppliers(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True, null=True)
    
# =======================
# ==== PRODUCTS =========
# =======================

class Products(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    statut = models.TextChoices("Enabled", "Disabled")
    quantity_in_stock = models.PositiveIntegerField(default=0)
    supplier = models.ForeignKey(Suppliers, on_delete=models.CASCADE)
    category = models.ManyToManyField(Categories, blank=True)
    date_added = models.DateTimeField()
    date_updated = models.DateTimeField()

# =========================================
# we'll leave it there for now 
# =========================================
 
"""

class Customers(...)

class Orders(...)

class OrderDetails(...)
    
"""