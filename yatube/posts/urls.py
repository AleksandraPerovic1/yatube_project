from django.urls import path
from . import views

urlpatterns = [
    # главная страница
    path('', views.index),
    # страница с постами отфильтрованными по группам
    path('group/<slug:slug>/', views.group_posts)
] 