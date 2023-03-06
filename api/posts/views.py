from rest_framework.response import Response
from rest_framework.views import APIView
from posts.models import *
from .serializers import PostSerializer, PostdetailSerializer
from rest_framework import status
from services.service import *
from posts.updater import updatePost
from django.contrib.auth.models import User


class HomePageView(APIView):
    def get(self, request):
        # ip_addr = request.META["REMOTE_ADDR"]
        # signUp(ip_addr)
        posts = Post.objects.all().order_by("-createdAt")
        hotPosts = Post.objects.all()
        postSerializer = PostSerializer(posts, many=True)
        hotPostSerializer = PostSerializer(hotPosts, many=True)
        return Response({"newPosts":postSerializer.data, "hotPosts":hotPostSerializer.data})


class PostListView(APIView):
    def get(self, request):
        ip_addr = request.META["REMOTE_ADDR"]
        posts = Post.objects.filter(category__in=postList(ip_addr)).order_by("-createdAt")
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class PostDetailView(APIView):
    def get(self, request, pk):
        ip_address = request.META["REMOTE_ADDR"]
        post = Post.objects.get(id=pk)
        seenAdd(ip_address, pk)
        addIntereset(ip_address,pk)
        serializer = PostdetailSerializer(post, many=False)
        return Response(serializer.data)


class PostLike(APIView):
    def patch(self, request, pk):
        ip_address = netaddr.IPAddress(request.META["REMOTE_ADDR"])
        post = Post.objects.get(id=pk)
        user = User.objects.get(username=ip_address.value)
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


