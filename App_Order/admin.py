from django.contrib import admin
from App_Order.models import Cart, Order


# Register your models here.
class AdminCart(admin.ModelAdmin):
    list_display = ['user', 'item', 'quantity', 'purchased', 'created', 'updated']


class AdminOrder(admin.ModelAdmin):
    list_display = ['user', 'ordered', 'created', 'orderId','paymentId']


admin.site.register(Cart, AdminCart)
admin.site.register(Order, AdminOrder)
