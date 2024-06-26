from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from blog.forms import MessageForm
from blog.models import Message


class MessageListView(ListView):
    model = Message
    # template_name = 'message_list.html'
    context_object_name = 'messages'

    def get_queryset(self):
        # Получаем только опубликованные записи
        return Message.objects.filter(is_published=True)


class MessageDetailView(DetailView):
    model = Message
    context_object_name = 'message'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        # Увеличиваем счетчик просмотров только если запись опубликована
        if obj.is_published:
            obj.views += 1
            obj.save()
        return obj


class MessageCreateView(CreateView):
    model = Message
    form_class = MessageForm

    def get_success_url(self):
        return reverse_lazy('message_detail', kwargs={'slug': self.object.slug})


class MessageUpdateView(UpdateView):
    model = Message
    form_class = MessageForm

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     if self.request.method == 'POST':
    #         context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
    #     else:
    #         context_data['formset'] = SubjectFormset(instance=self.object)
    #
    #     return context_data

    def get_success_url(self):
        return reverse_lazy('message_detail', kwargs={'slug': self.object.slug})


class MessageDeleteView(DeleteView):
    model = Message
    success_url = reverse_lazy('message_list')  # Перенаправление на страницу блога после удаления

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
