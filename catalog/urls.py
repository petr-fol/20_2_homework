from django.conf import settings
from django.urls import include
from django.conf.urls.static import static
from django.urls import path
from catalog.views import (ProductDetailView,
                           ProductUpdateView, ProductDeleteView, ProductCreateView, ProductListView)

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('detail/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('edit/<slug:slug>/', ProductUpdateView.as_view(), name='product_form'),
    path('confirm_delete/<pk>/', ProductDeleteView.as_view(), name='product_confirm_delete'),
    path('create/', ProductCreateView.as_view(), name='product_create'),


]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
