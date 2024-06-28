from itertools import count

from django import forms

from catalog.models import Product, ProductVersion
from config.style import StyleFormMixin


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['slug', 'category', "owner"]  # 'is_published', 'user'

    def clean_name(self):
        name = self.cleaned_data.get('name')
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in forbidden_words:
            if word in name:
                raise forms.ValidationError(f"Запрещенное слово '{word}' в названии продукта.")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in forbidden_words:
            if word in description:
                raise forms.ValidationError(f"Запрещенное слово '{word}' в описании продукта.")
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной.")
        return price


class VersionForm(forms.ModelForm):
    class Meta:
        model = ProductVersion
        fields = ['number_of_version', 'current_version']

    def clean_current_version(self):
        current_version = self.cleaned_data.get('current_version')
        if current_version:
            existing_current_version = ProductVersion.objects.filter(product=self.instance.product,
                                                              current_version=True).exclude(id=self.instance.id).first()
            if existing_current_version:
                raise forms.ValidationError("Может быть только одна текущая версия.")
        return current_version

