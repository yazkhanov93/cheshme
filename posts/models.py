from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
import blurhash
import numpy
from PIL import Image as IMG
from datetime import datetime, timezone


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="ady")

    class Meta:
        verbose_name_plural = "Kategoriýalar"

    def __str__(self):
        return self.title


class UserInterests(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="user")
    category = models.OneToOneField(Category, on_delete=models.CASCADE, verbose_name="category")
    count = models.IntegerField(verbose_name="sany")

    class Meta:
        ordering = ("-count",)
        verbose_name_plural = "User interes"

    def __str__(self):
        return str(self.user)

class Tag(models.Model):
    title = models.CharField(max_length=255, verbose_name="ady")

    class Meta:
        verbose_name_plural = "Taglar"

    def __str__(self):
        return self.title


class PostQuerySet(models.QuerySet):
    def hotness_ordering(self):
        return self.annotate(hotness=models.Count('like') + models.Count('seen') + models.F('share')).order_by('-hotness')


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db).hotness_ordering()


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category", verbose_name="kategoriýa", blank=True, null=True)
    title = models.CharField(max_length=255, verbose_name="ady")
    text = RichTextField(verbose_name="text")
    tagList = models.ManyToManyField(Tag, verbose_name="taglar", related_query_name="tagList")
    image = models.ImageField(upload_to="postImage/", verbose_name="surat")
    blurHash = models.CharField(max_length=255, verbose_name="blurhash", blank=True, null=True)
    seen = models.ManyToManyField(User,verbose_name="görülen sany", blank=True, related_name="seen")
    like = models.ManyToManyField(User,verbose_name="like sany", blank=True, related_name="likes")
    share = models.PositiveIntegerField(verbose_name="paýlaşylan sany", null=True, blank=True, default="0")
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name="goşulan güni")
    objects = PostManager()
    
    class Meta:
        verbose_name_plural="Makalalar"
        
    def __str__(self):
        return self.title

    def likes(self):
        return self.like.count()

    likes.short_description = "Like sany"
    likes.allow_tags = True

    def seens(self):
        return self.seen.count()

    def save(self, *args, **kwargs):
        blur = IMG.open(self.image).convert("RGB")
        self.blurHash = blurhash.encode(numpy.array(blur))
        super().save(*args, **kwargs)


    seens.short_description = "Görülen sany"
    seens.allow_tags = True
