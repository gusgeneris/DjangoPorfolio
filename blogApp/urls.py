from django.urls import path

from .views import render_posts,post,list_post_categoria

urlpatterns = [
    path("", render_posts, name='blog'),
    path('post/<int:id_post>', post),
    path('categoria/<int:id_categoria>', list_post_categoria)
]