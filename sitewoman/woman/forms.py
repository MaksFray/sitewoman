import re

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator

from .models import Category, Husband, Woman


class AddPostForm(forms.ModelForm):

    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="No category")
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), empty_label="Not married", required=False)

    class Meta:
        model = Woman
        fields = ['title', 'slug', 'content', 'is_published', 'category', 'husband']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
        }
        labels ={
            'slug': 'URL',
        }

class UploadFileForm(forms.Form):
    file = forms.FileField(label="File")