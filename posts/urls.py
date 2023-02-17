from django.urls import path
from .import views


urlpatterns = [
    path("", views.index, name="index"),
    path("post-detail/<int:pk>/", views.postDetail, name="post-detail"),
    path("post-like/<int:pk>/", views.likePost, name="post-like"),
    path("blog-list/", views.posts, name="blog-list"),
]