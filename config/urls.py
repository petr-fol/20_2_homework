from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from catalog.views import ProductDetailView, ProductUpdateView, ProductDeleteView, ProductCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('catalog.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
