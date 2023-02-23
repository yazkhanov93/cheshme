from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from services.service import *
from .filters import PostFilter
from django.contrib.auth.models import User
import netaddr


def index(request):
    ip_addr = request.META["REMOTE_ADDR"]
    signUp(ip_addr)
    post = Post.objects.all().order_by("-createdAt")
    myfilter = PostFilter(request.GET, queryset=post)
    post = myfilter.qs
    hottestPosts = Post.objects.all()
    context = {"posts":post, "hottestPosts":hottestPosts, "myfilter":myfilter}
    return render(request, "index.html", context)


def posts(request):
    ip_addr = request.META["REMOTE_ADDR"]
    posts = Post.objects.all().order_by("-createdAt")
    post = posts.filter(category__in=postList(ip_addr))
    myfilter = PostFilter(request.GET, queryset=posts)
    post = myfilter.qs
    resent_posts = Post.objects.all().order_by("-createdAt")[:4]
    context = {"posts":post, "myfilter":myfilter, "recent_posts":resent_posts, "tagList":tagList(), "categories":categoryList()}
    return render(request, "blog.html", context)


def postDetail(request, pk):
    ip_addr = request.META["REMOTE_ADDR"]
    post_detail = Post.objects.get(id=pk)
    seenAdd(ip_addr, pk)
    addIntereset(ip_addr, pk)
    posts = relatedPosts(pk)
    context = {"post_detail":post_detail, "posts":posts}
    return render(request, "post-details.html", context)


def likePost(request, pk):
    ip_addr = request.META["REMOTE_ADDR"]
    post = Post.objects.get(id=pk)
    user = User.objects.get(username=netaddr.IPAddress(ip_addr).value)
    if post.like.filter(username=user).exists():
        post.like.remove(user)
    else:
        post.like.add(user)
    return HttpResponseRedirect(reverse("post-detail", args=[str(pk)]))