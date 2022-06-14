# 탭을 공백4개 바꾸는 프로그램
import sys

first = sys.argv[1]
second = sys.argv[2]

with open(first, "r") as f:
    data = f.read()

with open(second, "w") as f:
    data2 = data.replace("\t", " " * 4)
    f.write(data2)
