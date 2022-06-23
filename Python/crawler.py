import requests
from bs4 import BeautifulSoup
from datetime import datetime

headers = {'User-Agent':''}
url = "https://datalab.naver.com/keyword/realtimeList.naver?age=20s"
response = requests.get(url, headers=headers)

# print(response)     # Response [200]
# print(response.text)      # html

soup = BeautifulSoup(response.text, 'html.parser')
rank = 1

# print(soup.title)
# print(soup.title.string)
# print(soup.span)
# print(soup.findAll('span'))

# file = open("daum.html", "w")
# file.write(response.text)
# file.close()

# html 문서에서 모든 a태그를 가져오는 코드
results = soup.findAll("span", "item_title")

search_rank_file = open("rankresult.txt", "w")

print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

for result in results:
    search_rank_file.write(str(rank) + "위" + result.get_text())
    print(rank,"위 : ", result.get_text(),"\n")
    rank += 1