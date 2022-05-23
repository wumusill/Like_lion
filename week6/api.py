import requests
import json

api = "https://api.openweathermap.org/data/2.5/weather?lat=36.6372&lon=127.4897&appid=14a3da618a241a46e1cb3f9aa07ef6a6&units=metric"
# &units=metric 화씨온도를 섭씨온도로 변경

result = requests.get(api)
print(result.text)

data = json.loads(result.text)
# print(type(data))

print(data["name"], "의 날씨입니다.")
print("날씨는", data["weather"][0]["main"], "입니다.")

# 현재온도
print("현재온도는", data["main"]["temp"], "입니다.")
# 체감온도
print("체감온도는", data["main"]["feels_like"], "입니다.")
# 최저온도
print("최저온도는", data["main"]["temp_min"], "입니다.")
# 최고온도
print("최고온도는", data["main"]["temp_max"], "입니다.")