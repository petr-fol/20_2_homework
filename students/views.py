from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from students.forms import StudentForm, SubjectForm
from students.models import Student, Subject


# Create your views here.
class StudentListView(ListView):
    model = Student
    template_name = 'students_list.html'
    context_object_name = 'students'


class StudentDetailView(DetailView):
    model = Student
    context_object_name = 'student'

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm

    def get_success_url(self):
        return reverse_lazy('student_detail', kwargs={'slug': self.object.slug})


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Student, Subject, form=SubjectForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)

        return context_data

    def get_success_url(self):
        return reverse_lazy('student_detail', kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('student_list')  # Перенаправление на страницу блога после удаления

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return HttpResponseRedirect(success_url)
