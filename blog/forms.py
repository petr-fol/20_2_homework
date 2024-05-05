from django import forms

from blog.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'description', 'image', ]  # 'author'
