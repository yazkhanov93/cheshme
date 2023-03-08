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


def signUp(userId):
    try:
        user = User.objects.create(
            username=userId,
            password=make_password(userId)
        )
        user.save()
    except:
        pass

def seenAdd(userId, pk):
    post = Post.objects.get(id=pk)
    user = User.objects.get(username=userId)
    if post.seen.filter(username=user).exists():
        pass
    else:
        post.seen.add(user)

def addIntereset(userId, pk):
    post = Post.objects.get(id=pk)
    user = User.objects.get(username=userId)
    interest = UserInterests.objects.filter(user=user)
    if len(interest) > 0:
        for i in interest:
            if i.user.username == userId and i.category == post.category:
                i.count = i.count + 1
                i.save()
            else:
                interest=UserInterests.objects.create(
                    user=user,
                    category=post.category,
                    count=1
                    )
                interest.save()
    else:
        interest=UserInterests.objects.create(
                    user=user,
                    category=post.category,
                    count=1
                    )
        interest.save()
    # except:
    #     for i in interest:
    #         if i.category == post.category:
    #             i.count +=1
    #             i.save()
    # finally:
    #     pass
    
def postList(userId):
    user = User.objects.get(username=userId)
    interests = UserInterests.objects.filter(user=user)
    interestList = []
    for i in interests:
        interestList.append(i.category)
    return interestList