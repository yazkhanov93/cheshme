from rest_framework.response import Response
from rest_framework.views import APIView
from posts.models import *
from .serializers import PostSerializer, PostdetailSerializer
from rest_framework import status
from services.service import *
from posts.updater import updatePost
from django.contrib.auth.models import User
import uuid


class HomePageView(APIView):
    def get(self, request):
        userId = None
        posts = Post.objects.all().order_by("-createdAt")
        if request.headers.get("Authorization"):
            pass
        else:
            userId = str(uuid.uuid1())
            signUp(userId)
        hotPosts = Post.objects.all()
        postSerializer = PostSerializer(posts, many=True)
        hotPostSerializer = PostSerializer(hotPosts, many=True)
        return Response({"userId":userId, "newPosts":postSerializer.data, "hotPosts":hotPostSerializer.data})


class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all().order_by("-createdAt")
        if request.headers.get("Authorization"):
            userId = request.headers.get("Authorization").split(" ")[-1]
            posts = posts.filter(category__in=postList(userId))
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class PostDetailView(APIView):
    def get(self, request, pk):
        userId = request.headers.get("Authorization").split(" ")[-1]
        addIntereset(userId, pk)
        seenAdd(userId, pk)
        post = Post.objects.get(id=pk)
        serializer = PostdetailSerializer(post, many=False)
        return Response(serializer.data)


class PostLike(APIView):
    def patch(self, request, pk):
        post = Post.objects.get(id=pk)
        user = User.objects.get(username=request.headers.get("Authorization").split(" ")[-1])
        if post.like.filter(username=user).exists():
            post.like.remove(user)
        else:
            post.like.add(user)
        post.save()
        return Response(status=status.HTTP_200_OK)


class PostShare(APIView):
    def patch(self, request, pk):
        post = Post.objects.get(id=pk)
        post.share = post.share + 1
        post.save()
        return Response(status=status.HTTP_200_OK) 


