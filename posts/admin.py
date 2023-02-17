from django.contrib import admin
from .models import *


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=["title",]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "likes", "seens", "share","createdAt"]