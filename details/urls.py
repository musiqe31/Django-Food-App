from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('<int:details>', views.details, name='details')
]
