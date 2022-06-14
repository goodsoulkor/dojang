# 페이징 구현
# def paging(m, n):
#     if m == 0:
#         print(0)
#     elif m % n == 0:
#         print(m // n)
#     else:
#         print(m // n + 1)


def paging(m, n):
    page = m // n
    if m % n != 0:
        page += 1
    print(page)


paging(0, 1)
paging(1, 1)
paging(2, 1)
paging(1, 10)
paging(10, 10)
paging(11, 10)
paging(10, 20)
