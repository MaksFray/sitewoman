from django.contrib import admin, messages
from .models import Woman, Category


@admin.register(Woman)
class WomanAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create', 'is_published', 'category', 'brief_info')
    list_display_links = ('title', )
    ordering = ('time_create', 'title')
    list_editable = ('is_published', 'category')
    list_per_page = 10
    actions = ['set_published', 'set_unpublished']
    search_fields = ['title', 'category__name']
    @admin.display(description="Short description", ordering="content")
    def brief_info(self, woman: Woman):
        return f"Description {len(woman.content)} symbols"

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