from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string

from woman.models import Woman, Category

MENU = ({'title': 'About', 'url_name': 'about'},
        {'title': 'Add page', 'url_name': 'add_page'},
        {'title': 'Contact', 'url_name': 'contact'},
        {'title': 'Login', 'url_name': 'login'},
        )


def index(request):
    posts = Woman.published.all()
    data = {
        'title': 'Home',
        'menu': MENU,
        'posts': posts,
        'category_selected': 0,
    }
    return render(request, 'woman/index.html', context=data)


def about(request):
    return render(request, 'woman/about.html')


def add_page(request):
    return HttpResponse("Add page")


def contact(request):
    return HttpResponse("Contact")


def login(request):
    return HttpResponse("Login")


def show_post(request, post_slug):
    post:Woman = get_object_or_404(Woman, slug=post_slug)
    data = {
        'title': post.title,
        'menu': MENU,
        'post': post,
        'category_selected': 1,
    }
    return render(request, 'woman/post.html', data)

def show_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = Woman.published.filter(category_id=category.pk)

    data = {
        'title': "Show by category",
        'menu': MENU,
        'posts': posts,
        'category_selected': category.pk,
    }
    return render(request, 'woman/index.html', context=data)

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")
