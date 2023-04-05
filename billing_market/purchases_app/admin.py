from django.contrib import admin
from .models import Vendor, Orders, OrderProducts


@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('vendor_id', 'vendor_name', 'vendor_contact', 'vendor_information', 'vendor_email', 'vendor_gst_number')


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'order_number', 'order_total_cost_without_gst', 'order_total_cost_with_gst', 'order_status', 'order_delivery_date', 'vendor')


@admin.register(OrderProducts)
class OrderProductsAdmin(admin.ModelAdmin):
    list_display = ('order_product_id', 'order_product', 'order_product_quantity', 'order_product_cost_per_quantity', 'order_product_total_cost', 'order_product_total_cost_with_gst')
