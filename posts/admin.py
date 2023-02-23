from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title",]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=["title",]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "likes", "seens", "share","createdAt"]
    # exclude = ["share"]

@admin.register(UserInterests)
class UserInterestsAdmin(admin.ModelAdmin):
    list_display = ["user", "category", "count"]