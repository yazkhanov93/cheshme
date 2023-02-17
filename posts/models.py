from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class UserId(models.Model):
    title = models.CharField(max_length=255, verbose_name="ady", unique=True)

    class Meta:
        verbose_name_plural="Ulanyjylar"

    def __str__(self):
        return self.title


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
    title = models.CharField(max_length=255, verbose_name="ady")
    text = RichTextField(verbose_name="text")
    tagList = models.ManyToManyField(Tag, verbose_name="taglar", related_query_name="tagList")
    image = models.ImageField(upload_to="postImage/", verbose_name="surat")
    seen = models.ManyToManyField(UserId,verbose_name="görülen sany", blank=True, related_name="gorulen")
    like = models.ManyToManyField(UserId,verbose_name="like sany", blank=True)
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

    seens.short_description = "Görülen sany"
    seens.allow_tags = True
