from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from .models import Woman, Category


class MarriageFilter(admin.SimpleListFilter):
    title = "Marriage status"
    parameter_name = "status"

    def lookups(self, request, model_admin):
        return [
            ('married', 'Married'),
            ('single', 'Single')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'married':
            return queryset.filter(husband__isnull=False)
        elif self.value() == 'single':
            return queryset.filter(husband__isnull=True)


@admin.register(Woman)
class WomanAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'photo', 'post_photo','content', 'category', 'husband', 'tags']
    prepopulated_fields = {'slug': ('title',), }
    readonly_fields = ['post_photo']
    filter_horizontal = ['tags']
    list_display = ('title', 'time_create', 'is_published', 'category', 'post_photo')
    list_display_links = ('title',)
    ordering = ('time_create', 'title')
    list_editable = ('is_published', 'category')
    list_per_page = 10
    actions = ['set_published', 'set_unpublished']
    search_fields = ['title', 'category__name']
    list_filter = [MarriageFilter, 'category__name', 'is_published']

    @admin.display(description="Short description", ordering="content")
    def brief_info(self, woman: Woman):
        return f"Description {len(woman.content)} symbols"

    @admin.display(description="Photo", ordering="content")
    def post_photo(self, woman: Woman):
        if woman.photo:
            return mark_safe(f"<img src='{woman.photo.url}' width=50>")
        else:
            return "No photo"

    def set_published(self, request, queryset):
        count = queryset.update(is_published=Woman.Status.PUBLISHED)
        self.message_user(request, f"{count} posts were updated")

    def set_unpublished(self, request, queryset):
        count = queryset.update(is_published=Woman.Status.DRAFT)
        self.message_user(request, f"{count} posts were updated", messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
