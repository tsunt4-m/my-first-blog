from django.conf import settings
from django.db import models
from django.utils import timezone

"""
ポストオブジェクトの状態（プロパティ）と命令（アクション）

Post
--------
title
text
author
created_date
published_date
publish()

"""

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)#他のモデルへのリンク?
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_data = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title