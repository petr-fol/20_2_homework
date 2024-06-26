from django import forms

from students.models import Subject, Student
from config.style import StyleFormMixin


class StudentForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'age']


class SubjectForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['title', 'description',]  # 'student'
