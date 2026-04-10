from django.db import models

# Create your models here.

class Director(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    about = models.TextField()
    experience = models.CharField(max_length=200)
    image = models.ImageField(upload_to='directors/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} - {self.role}"

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('pharmaceutical_tablet', 'Pharmaceutical Tablet'),
        ('artesunate_injection', 'Artesunate Injection'),
        ('surgical_instruments', 'Surgical Instruments'),
        ('ibuprofen', 'Ibuprofen'),
        ('desi_chicks', 'Desi Chicks'),
        ('optical_instruments', 'Optical Instruments'),
        ('amoxicillin_syrup', 'Amoxicillin Syrup'),
        ('ceftriaxone', 'Ceftriaxone'),
        ('pantoprazole', 'Pantoprazole'),
    ]
    
    WAREHOUSE_CHOICES = [
        ('chennai', 'Chennai Main'),
        ('mumbai', 'Mumbai Branch'),
        ('delhi', 'Delhi Branch'),
        ('bangalore', 'Bangalore Branch'),
    ]
    
    STORAGE_CHOICES = [
        ('room_temperature', 'Room Temperature'),
        ('refrigerated', 'Refrigerated (2-8°C)'),
        ('frozen', 'Frozen (-18°C or below)'),
        ('cool_dry', 'Cool & Dry'),
    ]
    
    # Basic Information
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    type = models.CharField(max_length=100, blank=True, null=True)
    strength = models.CharField(max_length=100, blank=True, null=True)
    
    # Pricing
    mrp_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    trade_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    retail_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    # Inventory
    stock = models.IntegerField(default=0)
    reorder_level = models.IntegerField(default=10)
    min_order_quantity = models.IntegerField(default=1)
    max_order_quantity = models.IntegerField(default=100)
    
    # Product Details
    manufacturer = models.CharField(max_length=200, blank=True, null=True)
    brand = models.CharField(max_length=200, blank=True, null=True)
    sku = models.CharField(max_length=100, blank=True, null=True)
    batch_number = models.CharField(max_length=100, blank=True, null=True)
    composition = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    expiry_date = models.DateField(blank=True, null=True)
    shelf_life = models.IntegerField(blank=True, null=True)
    
    # Warehouse & Storage
    warehouse_location = models.CharField(max_length=20, choices=WAREHOUSE_CHOICES, blank=True, null=True)
    storage_conditions = models.CharField(max_length=20, choices=STORAGE_CHOICES, blank=True, null=True)
    
    # Media
    product_image = models.ImageField(upload_to='products/', blank=True, null=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} - {self.get_category_display()}"
