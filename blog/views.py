from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from blog.forms import MessageForm
from blog.models import Message


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    context_object_name = 'messages'
    # permission_required = 'blog.view_message'

    def get_queryset(self):
        # Получаем только опубликованные записи
        return Message.objects.filter(is_published=True)


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    context_object_name = 'message'
    # permission_required = 'blog.view_message'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        # Увеличиваем счетчик просмотров только если запись опубликована
        if obj.is_published:
            obj.views += 1
            obj.save()
        return obj


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    # permission_required = 'blog.add_message'

    def get_success_url(self):
        return reverse_lazy('message_detail', kwargs={'slug': self.object.slug})


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    # permission_required = 'blog.change_message'

    def get_success_url(self):
        return reverse_lazy('message_detail', kwargs={'slug': self.object.slug})


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('message_list')  # Перенаправление на страницу блога после удаления
    # permission_required = 'blog.delete_message'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
