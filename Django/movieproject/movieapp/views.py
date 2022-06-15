from django.shortcuts import render
from .moviesecrets import my_id
import requests
import json

my_id = my_id()

def home(request):

    url = 'https://api.themoviedb.org/3/trending/movie/week?api_key=' + my_id
    # 응답 객체 그 자체
    response = requests.get(url)    
    # 응답 객체에서 가공해서 활용하고 싶은 데이터, json data
    resdata = response.text
    # json을 python 객체로 변환
    obj = json.loads(resdata)
    obj = obj['results']
    return render(request, 'index.html', {'obj':obj})
    