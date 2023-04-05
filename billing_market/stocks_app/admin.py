from django.contrib import admin
from .models import GST, Offers, Product, ProductCategory


@admin.register(GST)
class GSTAdmin(admin.ModelAdmin):
    list_display = ('gst_id', 'hsn_code', 'cgst', 'sgst', 'igst')


@admin.register(Offers)
class OffersAdmin(admin.ModelAdmin):
    list_display = ('offer_id', 'offer_name', 'offer_description', 'offer_in_percentile', 'offer_in_rupees', 'offer_start_date', 'offer_end_date')


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('product_category_id', 'product_category_name')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_name', 'product_cost_per_quantity', 'product_cost_with_gst', 'product_category', 'product_offers', 'product_quantity', 'product_total_cost', 'product_gst')