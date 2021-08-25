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