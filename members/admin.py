from django.contrib import admin
from .models import Director, Product

# Register your models here.

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'experience', 'created_at')
    list_filter = ('role', 'created_at')
    search_fields = ('name', 'role', 'about')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'type', 'strength', 'mrp_price', 'stock', 'created_at')
    list_filter = ('category', 'type', 'created_at')
    search_fields = ('name', 'manufacturer', 'brand', 'sku')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)
    list_per_page = 20
