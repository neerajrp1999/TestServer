from django.contrib import admin
from django.urls import path
from . import view

urlpatterns = [
    path('test',view.api_test)
]
