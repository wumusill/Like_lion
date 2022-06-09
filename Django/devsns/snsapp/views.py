from django.shortcuts import redirect, render
from .forms import PostForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

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