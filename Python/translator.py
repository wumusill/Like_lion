from googletrans import Translator

# 번역기 생성
translator = Translator()

# 번역할 문장 입력
sentence = input("번역할 문장을 입력하세요. : ")
lang = input("어떤 언어로 번역할까요? : ")

# 언어 감지 
detected = translator.detect(sentence)

# translate(text, dest, (src))
result = translator.translate(sentence, lang)

print("=========출 력 결 과=========")
print(detected.lang, ":", sentence)
print(result.dest, ":", result.text)
print("===========================")