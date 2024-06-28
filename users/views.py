import secrets
from django.shortcuts import get_object_or_404, redirect
from config.settings import EMAIL_HOST_USER
from django.views.generic import CreateView, UpdateView
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        # Сохраняем пользователя, но не коммитим его в базу данных
        user = form.save(commit=False)
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
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


class UserUpdateView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()

    return redirect(reverse("users:login"))
