from django.urls import path

from .views import render_posts,post

urlpatterns = [
    path("", render_posts, name='blog'),
    path('post/<int:id_post>', post)
]