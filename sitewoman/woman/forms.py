from django import forms
from .models import Category, Husband

class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255)
    slug = forms.SlugField(max_length=255, label="URL")
    content = forms.CharField(widget=forms.Textarea(), required=False)
    is_published = forms.BooleanField(required=False, label="Status", initial=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="No category")
    husband = forms.ModelChoiceField(queryset=Husband.objects.all(), empty_label="Not married")