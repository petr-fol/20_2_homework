from xml.etree.ElementInclude import include

from django.conf import settings
from django.conf.urls.static import static
# from django.contrib import admin
from django.urls import path

from catalog.views import index

urlpatterns = [
    path('', index),
]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

