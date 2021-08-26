import requests
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}  # USER AGENT STRING을 GOOGLE에서 검색한 후 나오는 'WHAT IS YOUR AGENT?'라는 사이트에서 가져온 브라우저 주소 입력
res = requests.get("http://naver.com", headers=headers)
res.raise_for_status()  # 응답 코드가 200이 아닌 경우 실행 종료
with open("NewNaverFile.html", "w", encoding="utf8") as f:  # 내가 원하는 종류의 새로운 파일 생성
    f.write(res.text)
