# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys

import urllib.request
import json
from apitestsecret import function

client_id = function("client_id")
client_secret = function("client_secret")

encText = urllib.parse.quote("한국")
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
# query는 필수 입력 요소
url = "https://openapi.naver.com/v1/search/cafearticle.json?query=" + encText

# url에 요청을 보낼 때 필요한 부가정보
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)

response = urllib.request.urlopen(request)

rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    # print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)

resdata = response_body.decode('utf-8')

# json 파일로 내보내기
# with open('movie.json', 'w', encoding='UTF-8-sig') as file:
#     file.write(json.dumps(resdata, ensure_ascii=False))

pydata = json.loads(resdata)
data = pydata['items']

print(data)