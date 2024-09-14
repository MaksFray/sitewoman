from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string

MENU = ['About', 'Add article', 'Callback', 'Login']

def index(request):
    data = {
        'title': 'Home',
        'menu': MENU,
    }
    return render(request, 'woman/index.html', context=data)

def about(request):
    return render(request, 'woman/about.html')

def categories_by_id(request, cat_id):
    return HttpResponse(f"<h1>Test</h1> cat_id: {cat_id}")

def categories_by_slug(request, cat_slug):
    return HttpResponse(f"<h1>Test</h1> cat_slug: {cat_slug}")
def archive(request, year):
    if year > 2024:
        uri = reverse('cats_slug', args=("music", ))
        return redirect(uri)
    return HttpResponse(f"Year: {year}")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")
