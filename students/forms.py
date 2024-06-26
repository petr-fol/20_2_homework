from django import forms

from students.models import Subject, Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'surname', 'age']


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['title', 'description',]  # 'student'
