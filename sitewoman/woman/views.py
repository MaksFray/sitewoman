from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string

from woman.models import Woman

MENU = ({'title': 'About', 'url_name': 'about'},
        {'title': 'Add page', 'url_name': 'add_page'},
        {'title': 'Contact', 'url_name': 'contact'},
        {'title': 'Login', 'url_name': 'login'},
        )


def index(request):
    data = {
        'title': 'Home',
        'menu': MENU,
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


def show_post(request, post_id):
    post:Woman = get_object_or_404(Woman, pk=post_id)
    data = {
        'title': post.title,
        'menu': MENU,
        'post': post,
        'cat_selected': 1,
    }
    return render(request, 'woman/post.html', data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")
