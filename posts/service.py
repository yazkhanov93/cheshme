from .models import *
from django.forms import ModelForm
from django.contrib.auth.models import User


def seenAdd(userId, postId):
    post = Post.objects.get(id=postId)
    user = User.objects.filter(username=userId)
    print(user.id)
    # if post.seen.filter(user_id=user.id).exists():
    #     pass
    # else:
    #     post.seen.add(user)


def relatedPosts(postId):
    posts = Post.objects.all()
    post = posts.get(id=postId)
    relatedPost = []
    for i in posts:
        if any(x in post.tagList.all().values() for x in i.tagList.all().values()):
            if i.id != post.id:
                relatedPost.append(i)
    return relatedPost


def tagList():
    tagList = Tag.objects.all()
    return tagList
    