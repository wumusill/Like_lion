from dataclasses import field
from django import forms
from .models import FreeComment, FreePost, Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        # form의 기반이 되는 모델
        model = Post
        # 입력받을 값
        fields = '__all__'
        # fields = ['title', 'body']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs = {
            'class':'form-control',
            'placeholder':"글 제목을 입력해주세요",
            'rows':20
        }

        self.fields['body'].widget.attrs = {
            'class':'form-control',
            'placeholder':"본문을 입력해주세요",
            'rows':20,
            'cols': 100
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields['comment'].widget.attrs = {
            'class':'form-control',
            'placeholder':"댓글을 입력해주세요",
            'rows':10
        }


class FreePostForm(forms.ModelForm):
    class Meta:
        # form의 기반이 되는 모델
        model = FreePost
        # 입력받을 값
        # fields = '__all__'
        fields = ['title', 'body']

    def __init__(self, *args, **kwargs):
        super(FreePostForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs = {
            'class':'form-control',
            'placeholder':"글 제목을 입력해주세요",
            'rows':20
        }

        self.fields['body'].widget.attrs = {
            'class':'form-control',
            'placeholder':"본문을 입력해주세요",
            'rows':20,
            'cols': 100
        }


class FreeCommentForm(forms.ModelForm):
    class Meta:
        model = FreeComment
        fields = ['comment']
    
    def __init__(self, *args, **kwargs):
        super(FreeCommentForm, self).__init__(*args, **kwargs)

        self.fields['comment'].widget.attrs = {
            'class':'form-control',
            'placeholder':"댓글을 입력해주세요",
            'rows':10
        }