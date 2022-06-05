from django.shortcuts import render, redirect
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

# 블로그 글 작성 html을 보여주는 함수
def new(request):
    return render(request, 'new.html')

# 블로그 글을 저장해주는 함수
def create(request):
    if(request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')

# django form을 이용해 입력값을 받는 함수
# GET 요청과 (= 입력값을 받을 수 있는 html을 갖다 줘야 함) 
# POST 요청 (= 입력한 내용을 데이터베이스에 저장. form에서 입력한 내용을 처리)
# 둘 다 처리가 가능한 함수 
def formcreate(request):
    if request.method == 'POST':
        # 입력 내용을 DB에 저장
        form = BlogForm(request.POST)
        if form.is_valid():
            # 저장하는 코드
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')
    else:
        # 입력 받을 수 있는 html을 갖다 주기
        form = BlogForm()
    # render()의 세 번째 인자로 views.py 내의 데이터를 html에 넘겨줄 수 있습니다. 단, 딕셔너리 자료형으로 넘거주어야 함
    return render(request, 'form_create.html', {'form':form})

def modelformcreate(request):
    if request.method == 'POST':
        # 입력 내용을 DB에 저장
        form = BlogModelForm(request.POST)
        if form.is_valid():
            # 저장하는 코드
            form.save()
            return redirect('home')
    else:
        # 입력 받을 수 있는 html을 갖다 주기
        form = BlogModelForm()
    return render(request, 'form_create.html', {'form':form})