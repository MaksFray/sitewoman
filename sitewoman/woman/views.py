from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    return HttpResponse("Main page")

def categories(request, cat_id):
    return HttpResponse(f"<h1>Test</h1> cat_id: {cat_id}")

def archive(request, year):
    return HttpResponse(f"Year: {year}")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Page not found</h1>")