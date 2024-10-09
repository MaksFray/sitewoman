import re

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator

from .models import Category, Husband

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255, min_length=5,
                            widget=forms.TextInput(attrs={'class': 'form-input'}),
                            error_messages={
                                'min_length': 'Too short title',
                                'required': 'Input title',
                            })
    slug = forms.SlugField(max_length=255, label="URL",
                           validators=[
                               MinLengthValidator(5, message="Length must be more than 5 symbols"),
                               MaxLengthValidator(100, message="Length must be less than 5 symbols"),
                           ])
    content = forms.CharField(widget=forms.Textarea(attrs={'cols':50, 'rows': 5}), required=False)
    is_published = forms.BooleanField(required=False, label="Status", initial=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="No category")
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), empty_label="Not married", required=False)

    def clean_title(self):
        title = self.cleaned_data['title']
        pattern = r'^[а-яА-ЯёЁa-zA-Z0-9., ]+$'
        if not(re.fullmatch(pattern, title)):
            raise ValidationError("Wrong symbols in title")