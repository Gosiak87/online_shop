from django.contrib import admin
from .models import Category, Product

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'price', 'stock', 'available', 'created', 'update', 'category']
    list_filter = ['available', 'created', 'update', 'category']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
