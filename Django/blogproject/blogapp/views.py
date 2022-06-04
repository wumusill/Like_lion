from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

# 블로그 글 작성 html을 보여주는 함수
def new(request):
    return render(request, 'new.html')

# 블로그 글을 저장해주는 함수
def create(request):
    
    
    
    return