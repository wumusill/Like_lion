from tkinter import PROJECTING
from django.shortcuts import redirect, render, get_object_or_404
from .forms import PostForm, CommentForm
from .models import Post

# Create your views here.
def home(request):
    # Post에 있는 모든 객체들을 가져오는 코드
    # posts = Post.objects.all()
    # Post의 객체를 filter를 통해 가져오는 코드
    posts = Post.objects.filter().order_by('-date')
    return render(request, 'index.html', {'posts':posts})

def postcreate(request):
    # request method가 POST일 경우
        # 입력값 저장
    
    # request method가 GET일 경우
        # form 입력 html 띄우기
    if request.method == 'POST' or request.method == 'FILES':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    # post_form.html을 열고 객체 form을 'form'이란 이름으로 함께 보냄
    return render(request, 'post_form.html', {'form':form})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    comment_form = CommentForm()
    return render(request, 'detail.html', {'post_detail':post_detail, 'comment_form':comment_form})

# 댓글 저장
def new_comment(request, post_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Post, pk=post_id)
        finished_form.save()
    return redirect('detail', post_id)