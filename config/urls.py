from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from catalog.views import product_detail, edit_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')),
    path('product_detail/<int:product_id>/', product_detail, name='product_detail'),
    path('edit_product/<int:product_id>/', edit_product, name='edit_product')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
