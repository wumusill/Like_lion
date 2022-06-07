from django.shortcuts import redirect, render
from django.contrib import auth     # 특정 유저 개체가 DB에 저장되어 있는지 아닌지 판단, 로그인/로그아웃 기능 수행

def login(request):
    # POST 요청이 들어오면 로그인 처리
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
        # 실제 있는 데이터인지 확인하는 코드, 있는 개체라면 유저 개체를 반환하고, 없다면 None을 반환
        user = auth.authenticate(request, username=userid, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')
        
    # GET 요청이 들어오면 login form 을 담고 있는 login.html을 띄워주는 역할
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')