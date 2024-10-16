from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template.loader import render_to_string
from django.views import View
from django.views.generic import TemplateView

from woman.forms import AddPostForm, UploadFileForm
from woman.models import Woman, Category, Tag, UploadFiles

MENU = ({'title': 'About', 'url_name': 'about'},
        {'title': 'Add page', 'url_name': 'add_page'},
        {'title': 'Contact', 'url_name': 'contact'},
        {'title': 'Login', 'url_name': 'login'},
        )


def index(request):
    posts = Woman.published.all().select_related('category')
    data = {
        'title': 'Home',
        'menu': MENU,
        'posts': posts,
        'category_selected': 0,
    }
    return render(request, 'woman/index.html', context=data)


class WomanHome(TemplateView):
    template_name = 'woman/index.html'
    posts = Woman.published.all().select_related('category')
    extra_context = {
        'title': 'Home',
        'menu': MENU,
        'posts': posts,
        'category_selected': 0,
    }


def about(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            fp = UploadFiles(file=form.cleaned_data['file'])
            fp.save()
    else:
        form = UploadFileForm()
    return render(request, 'woman/about.html', {
        'title': 'About',
        'menu': MENU,
        'form': form,
    })


def add_page(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    data = {
        'title': 'Add post',
        'menu': MENU,
        # 'posts': posts,
        'category_selected': 0,
        'form': form,
    }
    return render(request, 'woman/add_page.html', context=data)


class AddPage(View):
    def get(self, request):
        form = AddPostForm()
        data = {
            'title': 'Add post',
            'menu': MENU,
            'form': form,
        }
        return render(request, 'woman/add_page.html', context=data)

    def post(self, request):
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        data = {
            'title': 'Add post',
            'menu': MENU,
            'form': form,
        }
        return render(request, 'woman/add_page.html', context=data)


def contact(request):
    return HttpResponse("Contact")


def login(request):
    return HttpResponse("Login")


def show_post(request, post_slug):
    post: Woman = get_object_or_404(Woman, slug=post_slug)
    data = {
        'title': post.title,
        'menu': MENU,
        'post': post,
        'category_selected': 1,
    }
    return render(request, 'woman/post.html', data)


def show_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = Woman.published.filter(category_id=category.pk).select_related('category')

    data = {
        'title': f"Show by category {category.name}",
        'menu': MENU,
        'posts': posts,
        'category_selected': category.pk,
    }
    return render(request, 'woman/index.html', context=data)


def show_tag_post_list(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = tag.tags.filter(is_published=Woman.Status.PUBLISHED).select_related('category')
    data = {
        'title': f"Tag {tag.tag}",
        'menu': MENU,
        'posts': posts,
        'category_selected': None,
    }

    return render(request, 'woman/index.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")
