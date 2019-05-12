from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('add/', views.add),
    path('about/', views.about),
    path('update/<int:todo_id>/', views.update, name='update'),
    path('edit/<int:todo_id>/', views.edit, name='edit'),
    path('delete/<int:todo_id>/', views.delete, name="delete"),
]
