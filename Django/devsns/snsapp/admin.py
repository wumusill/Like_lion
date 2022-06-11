from django.contrib import admin
from .models import FreeComment, FreePost, Post, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(FreePost)
admin.site.register(FreeComment)