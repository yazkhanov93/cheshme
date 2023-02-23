from django.urls import path, include
from api.posts.views import *

urlpatterns = [
    path("home/", HomePageView.as_view(), name="home"),
    path("posts/", PostListView.as_view(), name="posts"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post"),
    path("like/<int:pk>/", PostLike.as_view(), name="like"),
    path("share/<int:pk>/", PostShare.as_view(), name="share"),
]