import requests
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}



for year in range(2015, 2020):      # 2015년부터 2019년까지의 페이지 차례로 불러오기
    url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query={}%EB%85%84%20%EC%98%81%ED%99%94%20%EC%88%9C%EC%9C%84".format(year)
    res = requests.get(url, headers=headers)    # 이걸 해줘야 사용자 입장에서 접속하는 것으로 보이게 할 수 있다고 나는 그렇게 이해함
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    images = soup.find_all("img")

    for index, image in enumerate(images):
        print(image["src"])

        # 이미지 다운로드하기
        image_res = requests.get(image["src"])
        image_res.raise_for_status()

        with open("moive_{}_{}.jpg".format(index + 1, year), "wb") as f:    # {}를 하나만 쓰면, 년도가 변경될 때 마다 파일 이름이 중복되므로 덮어쓰기 된다. 따라서 year를 나타내는 {}까지 총 두 개를 써준다
            f.write(image_res.content)      # 이 리소스(res)가 가지고 있는 content의 정보를 파일로 작성하는것인데, 그 정보가 이미지이므로 이미지 저장

        # 여덟개의 사진만 가져오기 (출력하는게 위에있으므로 4번인덱스까지 출력 후 종료)
        if (index >= 7):
            break
