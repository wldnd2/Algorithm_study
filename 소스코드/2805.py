# 2805 나무 자르기
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
height = list(map(int, input().split()))
low, high = 1, max(height)

while low <= high:
    mid = (low+high) // 2
    result = 0
    for h in height:
        if h - mid > 0:
            result += h - mid
        # 입력수가 많고, n^2이므로 m보다 크다면 뒤에 것은 할 필요가 없으니 하지 않는다.
        if result > m:
            break
    if result >= m:
        low = mid + 1
    else:
        high = mid - 1
print(high)