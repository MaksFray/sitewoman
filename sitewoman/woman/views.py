from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Main page")

def categories(request, cat_id):
    return HttpResponse(f"<h1>Test</h1> cat_id: {cat_id}")

def archive(request, year):
    return HttpResponse(f"Year: {year}")