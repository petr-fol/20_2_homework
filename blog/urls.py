from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from blog.views import (MessageDetailView,
                        MessageUpdateView, MessageDeleteView, MessageCreateView, MessageListView)

urlpatterns = [
    path('', MessageListView.as_view(), name='message_list'),
    path('detail/<slug:slug>/', MessageDetailView.as_view(), name='message_detail'),
    path('edit/<slug:slug>/', MessageUpdateView.as_view(), name='message_form'),
    path('confirm_delete/<pk>/', MessageDeleteView.as_view(), name='message_confirm_delete'),
    path('create/', MessageCreateView.as_view(), name='message_create'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
