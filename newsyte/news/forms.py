from .models import Articals
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticalsForm(ModelForm):
    class Meta:
        model = Articals
        fields = ['title', 'anons', 'full_text', 'data']

        widgets ={
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            'data': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder':'Дата публикации'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            })
        }