from django.urls import path

from . import views

urlpatterns = [
    path('pages/index.html', views.index),
    path('pages/add.html', views.add),
    path('pages/edit.html', views.edit),
    path('pages/about.html', views.about),
]