from datetime import datetime,timezone
from apscheduler.schedulers.background import BackgroundScheduler
from .models import Post


def updatePost():
    posts = Post.objects.all()
    for post in posts:
        d = post.createdAt - datetime.now(timezone.utc)
        if d.days > 7:
            post.like//2
            post.share//2
            post.seen//2