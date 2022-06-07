from distutils.command.upload import upload
from django.db import models
from django.forms import model_to_dict

# Create your models here.
# DB에 저장되어야 하는 객체들을 만들어 준다.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    photo = models.ImageField(blank=True, null=True, upload_to='blog_photo')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    # 어떤 게시물에 달려있는 댓글인지 알 수 있는, 댓글이 달린 그 게시물이 쓰임, Blog 객체를 참조해서 만드는 컬럼
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment