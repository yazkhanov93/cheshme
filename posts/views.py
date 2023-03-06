from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from services.service import *
from .filters import PostFilter
from django.contrib.auth.models import User
import netaddr
import uuid
from django.core.paginator import Paginator


def index(request):
    userId = request.COOKIES.get("userId")
    if userId:
        pass
    else:
        userId = str(uuid.uuid1())
    signUp(userId)
    post = Post.objects.all().order_by("-createdAt")
    myfilter = PostFilter(request.GET, queryset=post)
    post = myfilter.qs
    hottestPosts = Post.objects.all()
    context = {"posts":post, "hottestPosts":hottestPosts, "myfilter":myfilter, "uuid":userId}
    return render(request, "index.html", context)


def postsByCategory(request, pk):
    posts = Post.objects.filter(category__title=pk)
    category = Category.objects.all().only("id","title")
    recent_posts = Post.objects.all().only("id","title","image","createdAt").order_by("-createdAt")[:4]
    context = {"posts":posts, "recent_post":recent_posts, "categories":category}
    return render(request, "category.html", context)


def posts(request):
    userId = request.COOKIES.get("userId")
    posts = Post.objects.all().order_by("-createdAt")
    post = posts.filter(category__in=postList(userId))
    myfilter = PostFilter(request.GET, queryset=posts)
    paginator = Paginator(myfilter.qs, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    recent_posts = Post.objects.all().only("id","title","image","createdAt").order_by("-createdAt")[:4]
    context = {"posts":page_obj, "myfilter":myfilter, "recent_posts":recent_posts, "tagList":tagList(), "categories":categoryList()}
    return render(request, "blog.html", context)


def postDetail(request, pk):
    userId = request.COOKIES.get("userId")
    post_detail = Post.objects.get(id=pk)
    seenAdd(userId, pk)
    addIntereset(userId, pk)
    posts = relatedPosts(pk)
    context = {"post_detail":post_detail, "posts":posts}
    return render(request, "post-details.html", context)


def likePost(request, pk):
    userId = request.COOKIES.get("userId")
    post = Post.objects.get(id=pk)
    user = User.objects.get(username=userId)
    if post.like.filter(username=user).exists():
        post.like.remove(user)
    else:
        post.like.add(user)
    return HttpResponseRedirect(reverse("post-detail", args=[str(pk)]))