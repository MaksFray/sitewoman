from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string

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
    return HttpResponse(f"Show post with id={post_id}")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")
