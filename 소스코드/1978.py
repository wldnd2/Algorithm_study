# 1978 소수 찾기
from math import sqrt


def prime(num):
    if num == 1:
        return False
    else:
        last = int(sqrt(num))+1
        for i in range(2, last):
            if num % i == 0:
                return False
        return True


int(input())
data = list(map(int, input().split()))
cnt = 0
for i in data:
    if prime(i):
        cnt += 1
print(cnt)
