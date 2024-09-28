from django.contrib import admin
from .models import Woman, Category


@admin.register(Woman)
class WomanAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published', 'category')
    list_display_links = ('id', 'title')
    ordering = ('time_create', 'title')
    list_editable = ('is_published', 'category')
    list_per_page = 10

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')