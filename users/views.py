from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from config.settings import EMAIL_HOST_USER
from django.views.generic import CreateView, UpdateView
from users.forms import UserRegisterForm, UserProfileForm
from django.urls import reverse_lazy
import string
import secrets
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from .models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    # permission_required = 'users.add_user'

    def form_valid(self, form):
        # Сохраняем пользователя, но не коммитим его в базу данных
        user = form.save(commit=False)
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save() # update_fields=['token','is_active']
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}'
        # Отправляем письмо для верификации
        subject = 'Подтверждение почты'
        message = f'Пожалуйста, перейдите по ссылке для верификации почты.{url}'
        from_email = EMAIL_HOST_USER
        to_email = form.cleaned_data['email']

        send_mail(subject, message, from_email, [to_email])

        # Коммитим пользователя в базу данных
        user.save()

        return super().form_valid(form)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')
    # permission_required = 'users.change_user'

    def get_object(self, queryset=None):
        return self.request.user


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()

    return redirect(reverse("users:login"))


def generate_password():
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(password_characters) for _ in range(10))
    return password


def reset_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = get_object_or_404(User, email=email)
        new_password = generate_password()
        user.set_password(new_password)
        user.save()
        send_mail(
            'Восстановление пароля',
            f'Здравствуйте! Ваш новый пароль: {new_password}',
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently=False,
        )
        return redirect(reverse('users:reset_password_done'))
    return render(request, 'users/reset_password.html')
