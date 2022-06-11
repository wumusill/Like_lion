from django.shortcuts import redirect, render
# 로그인 로그아웃을 구현하기 위한 import
from django.contrib import auth
# 회원가입 처리를 위한 import
from django.contrib.auth.models import User

def login(request):
    # request == POST
    # 로그인 시키기
    
    # request == GET
    # login.html 띄우기

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        # authenticate가 존재하는 회원이라면 회원 객체를 반환하고 아니라면 None을 반환
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'bad_login.html')

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home') 

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['repeat']:
            # 회원가입
            new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            # 로그인
            auth.login(request, new_user)
            # 홈으로 리다이렉션
            return redirect('home')
    return render(request, 'register.html')