from django.contrib import admin

from catalog.models import Product, Version

admin.site.register(Product)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('number_of_version', 'current_version', 'product')
    list_filter = ('number_of_version',)
