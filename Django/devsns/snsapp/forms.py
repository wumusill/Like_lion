from dataclasses import field
from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        # form의 기반이 되는 모델
        model = Post
        # 입력받을 값
        fields = '__all__'
        # fields = ['title', 'body']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']