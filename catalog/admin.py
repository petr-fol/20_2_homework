from django.contrib import admin

from catalog.models import Product, ProductVersion

admin.site.register(Product)


@admin.register(ProductVersion)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('number_of_version', 'current_version', 'product')
    list_filter = ('number_of_version',)
