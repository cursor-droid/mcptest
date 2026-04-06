from django.contrib import admin

from catalog.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "price", "quality", "stock", "is_active")
    list_filter = ("is_active", "quality")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "description")
