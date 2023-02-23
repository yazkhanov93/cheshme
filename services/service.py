from posts.models import *
from django.contrib.auth.models import User
import netaddr
from django.contrib.auth.hashers import make_password


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

def categoryList():
    categories = Category.objects.all()
    return categories


def signUp(ip_addr):
    try:
        userName = netaddr.IPAddress(ip_addr)
        user = User.objects.create(
            username=userName.value,
            password=make_password(str(userName.value))
        )
        user.save()
    except:
        pass

def seenAdd(ip_addr, pk):
    post = Post.objects.get(id=pk)
    username = netaddr.IPAddress(ip_addr)
    user = User.objects.get(username=username.value)
    if post.seen.filter(username=user).exists():
        pass
    else:
        post.seen.add(user)

def addIntereset(ip_addr, pk):
    post = Post.objects.get(id=pk)
    user = User.objects.get(username=netaddr.IPAddress(ip_addr).value)
    interest = UserInterests.objects.filter(user=user)
    try:
        interest=UserInterests.objects.create(
            user=user,
            category=post.category,
            count=1
            )
        interest.save()
    except:
        for i in interest:
            if i.category == post.category:
                i.count +=1
                i.save()
    finally:
        pass
    
def postList(ip_addr):
    user = User.objects.get(username=netaddr.IPAddress(ip_addr).value)
    interests = UserInterests.objects.filter(user=user)
    interestList = []
    for i in interests:
        interestList.append(i.category)
    return interestList