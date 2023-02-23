from rest_framework import serializers
from posts.models import Post, Category, Tag


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)
    class Meta:
        model = Post
        fields = ["id", "title", "category", "image", "likes", "seens", "share"]


class PostdetailSerializer(serializers.ModelSerializer):
    tagList = TagListSerializer(many=True)
    class Meta:
        model = Post
        fields = ["id", "title", "text", "category", "image", "tagList", "likes", "seens", "share", "createdAt"]