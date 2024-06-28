from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import TemplateView

from users.apps import UsersConfig
from users.views import UserCreateView, UserUpdateView, email_verification, reset_password

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('reset-password/', reset_password, name='reset-password'),
    path('reset-password/done/', TemplateView.as_view(template_name='users/reset_password_done.html'),
         name='reset_password_done'),

]
