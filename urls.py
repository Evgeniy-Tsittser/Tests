from django.contrib import admin
from django.urls import path
from .views import blog_views

urlpatterns = [
    path('', blog_views, name='home')
]