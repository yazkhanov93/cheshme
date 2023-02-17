from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from .service import seenAdd, relatedPosts, tagList
from .filters import PostFilter

def index(request):
    ip_address = request.META["REMOTE_ADDR"]
    try:
        user = UserId.objects.create(
            title=ip_address
        )
        user.save()
    except:
        pass
    post = Post.objects.all().order_by("-createdAt")
    myfilter = PostFilter(request.GET, queryset=post)
    post = myfilter.qs
    hottestPosts = Post.objects.all()
    context = {"posts":post, "hottestPosts":hottestPosts, "myfilter":myfilter}
    return render(request, "index.html", context)


def posts(request):
    ip_address = request.META["REMOTE_ADDR"]
    try:
        user = UserId.objects.create(
            title=ip_address
        )
        user.save()
    except:
        pass
    post = Post.objects.all().order_by("-createdAt")
    myfilter = PostFilter(request.GET, queryset=post)
    post = myfilter.qs
    resent_posts = Post.objects.all().order_by("-createdAt")[:4]
    context = {"posts":post, "myfilter":myfilter, "recent_posts":resent_posts, "tagList":tagList()}
    return render(request, "blog.html", context)


def postDetail(request, pk):
    ip_address = request.META["REMOTE_ADDR"]
    post_detail = Post.objects.get(id=pk)
    seenAdd(ip_address, pk)
    posts = relatedPosts(pk)
    context = {"post_detail":post_detail, "posts":posts}
    return render(request, "post-details.html", context)


def likePost(request, pk):
    ip_address = request.META["REMOTE_ADDR"]
    post = Post.objects.get(id=pk)
    user = UserId.objects.get(title=ip_address)
    if post.like.filter(title=user).exists():
        post.like.remove(user)
    else:
        post.like.add(user)
   
    return HttpResponseRedirect(reverse("post-detail", args=[str(pk)]))