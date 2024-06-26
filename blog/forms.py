from django import forms
from blog.models import Message
from config.style import StyleFormMixin


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'description', 'image', 'is_published']  # 'author'

