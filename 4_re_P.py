import re

p = re.compile("ca.e")
# . : 하나의 문자를 의미    ex) ("ca.e") = care, cafe, case, ...
# ^ : 문자열의 시작         ex) ("^de") = desk, destination, ...
# $ : 문자열의 끝           ex) ("se$") = case, base, ...

m = p.match("careless")

def print_match(m):
    if m:
        print("매칭")
    else:
        print("매칭되지 않음")

print_match(m)

m.group()   # 일치하는 문자열 반환
m.string()  # 입력받은 문자열
m.start()   # 일치하는 문자열의 시작 index
m.end()     # 일치하는 문자열의 끝 index
m.span()    # 일치하는 문자열의 시작&끝 index

lst = p.findall("good care cafe") # 일치하는 모든 것을 리스트 형태로 반환
print(lst)     # [care, cafe] 출력

# 정리
# 1. p = re.compile(“원하는 형태”)
# 2. m = p.match(“비교할 문자열”) : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search(“비교할 문자열”) : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall(“비교할 문자열”) : 일치하는 모든 것을 “리스트” 형태로 반환