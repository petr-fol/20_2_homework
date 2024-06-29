from django.contrib import admin

from catalog.models import Product, ProductVersion, ProductCategory

admin.site.register(Product)


@admin.register(ProductVersion)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('number_of_version', 'current_version', 'product')
    list_filter = ('number_of_version',)


@admin.register(ProductCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name',)
