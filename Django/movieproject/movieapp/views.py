from django.shortcuts import render
from .moviesecrets import my_id
import requests
import json
from .forms import SearchForm

my_id = my_id()

def home(request):
    if request.method == 'POST':
        # 입력된 내용을 바탕으로
        # https://api.themoviedb.org/3/search/movie?api_key=<<api_key>>&language=en-US&query=search&page=1&include_adult=false
        # 위 형태의 url로 get 요청 보내기
        form = SearchForm(request.POST)
        searchword = request.POST.get('search')
        if form.is_valid():
            url = 'https://api.themoviedb.org/3/search/movie?api_key='+ my_id + '&query=' + searchword
            response = requests.get(url)
            resdata = response.text
            obj = json.loads(resdata)
            obj = obj['results']
            return render(request, 'search.html', {'obj':obj})
    else:
        form = SearchForm()
        url = 'https://api.themoviedb.org/3/trending/movie/week?api_key=' + my_id
        # 응답 객체 그 자체
        response = requests.get(url)    
        # 응답 객체에서 가공해서 활용하고 싶은 데이터, json data
        resdata = response.text
        # json을 python 객체로 변환
        obj = json.loads(resdata)
        obj = obj['results']
    return render(request, 'index.html', {'obj':obj, 'form':form})
    
def detail(request, movie_id):

    url = 'https://api.themoviedb.org/3/movie/' + movie_id + '?api_key=' + my_id
    response = requests.get(url)
    resdata = response.text

    return render(request, 'detail.html', {"resdata":resdata})

def base(request):
    return render(request, 'base.html')