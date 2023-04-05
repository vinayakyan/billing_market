from django.contrib import admin
from .models import Customer, Invoice, InvoiceProducts


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'customer_name', 'customer_contact', 'customer_address')


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_id', 'invoice_number', 'customer', 'total_cost_without_gst', 'total_cost_with_offers_and_gst', 'total_cost_with_gst', 'invoice_created_by')


@admin.register(InvoiceProducts)
class InvoiceProductsAdmin(admin.ModelAdmin):
    list_display = ('invoice_product_id', 'product_invoice', 'invoice_product_quantity', 'invoice_product_cost_per_quantity', 'invoice_product_total_cost', 'invoice_product_cost_per_quantity_with_offer', 'invoice_product_total_cost_with_gst', 'invoice_product_total_cost_with_offer')
