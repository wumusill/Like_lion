from django.db import models
from django.conf import settings

# 게시물 모델
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # Post를 참조하는 외래키
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment