from django import template
import woman.views as views
from woman.models import Category

register = template.Library()
@register.inclusion_tag('woman/list_categories.html')
def show_categories(category_selected=0):
    categories = Category.objects.all()
    return {'categories': categories, 'category_selected':category_selected}