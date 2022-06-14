# 사이냅소프트 면접문제
"""
주어진 문자열(공백 없이 쉼표로 구분되어 있음)을 가지고 아래 문제에 대한 프로그램을 작성하세요.

이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌
"""
strName = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"

names = strName.split(",")

# 1. 김씨와 이씨는 각각 몇 명 인가요?
# 풀이 1. startwith() 사용
numKim = 0
numLee = 0
for name in names:
    if name.startswith("김"):
        numKim += 1
    elif name.startswith("이"):
        numLee += 1

print("김씨는 총 {}명 입니다.".format(numKim))
print("이씨는 총 {}명 입니다.".format(numLee))

# 풀이 2. 인덱싱 사용
# numKim = 0
# numLee = 0
# for name in names:
#     if name[0] == "김":
#         numKim += 1
#     elif name[0] == "이":
#         numLee += 1

# print("김씨는 총 {}명 입니다.".format(numKim))
# print("이씨는 총 {}명 입니다.".format(numLee))
print()

# 2. "이재영"이란 이름이 몇 번 반복되나요?
numLJY = 0
for name in names:
    if name == "이재영":
        numLJY += 1

print("이재영 이라는 이름은 총 %d번 반복 됩니다." % numLJY)
print()

# 3. 중복을 제거한 이름을 출력하세요.
setNames = list(set(names))
print(setNames)

# 4. 중복을 제거한 이름을 오름차순으로 정렬하여 출력하세요.
# print(sorted(setNames))
setNames.sort()
print(setNames)
