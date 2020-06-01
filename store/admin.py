from django.contrib import admin
from .models import Customer,Product,Order,OrderItem,ShippingAddress
# Register your models here.

@admin.register(Customer)
class customerAdmin(admin.ModelAdmin):
    '''Admin View for customer'''
    pass
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''Admin View for Product'''
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    '''Admin View for Order'''
    pass
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    '''Admin View for OrderItem'''
    pass

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    '''Admin View for ShippingAddress'''
    pass