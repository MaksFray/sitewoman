from django.urls import path, re_path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('cat/<int:cat_id>/', views.categories_by_id, name="cats_id"),
    path('cat/<str:cat_slug>/', views.categories_by_slug, name="cats_slug"),
    path('archive/<year4:year>/', views.archive, name="archive"),
]