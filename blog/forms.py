from django import forms
from blog.models import Subject
from blog.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'description', 'image', 'is_published']  # 'author'


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['title', 'description',]  # 'student'
