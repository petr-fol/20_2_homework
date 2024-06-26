from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from students.views import StudentListView, StudentDetailView, StudentUpdateView, StudentDeleteView, StudentCreateView

urlpatterns = [
    path('', StudentListView.as_view(), name='student_list'),
    path('detail/<slug:slug>/', StudentDetailView.as_view(), name='student_detail'),
    path('edit/<slug:slug>/', StudentUpdateView.as_view(), name='student_form'),
    path('confirm_delete/<pk>/', StudentDeleteView.as_view(), name='student_confirm_delete'),
    path('create/', StudentCreateView.as_view(), name='student_create'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
