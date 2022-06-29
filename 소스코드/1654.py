# 1654 랜선 자르기
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
length = [int(input()) for i in range(k)]
low, high = 1, max(length)
while low <= high:
    mid = (low+high) // 2
    cnt = sum([i//mid for i in length])
    if cnt >= n:
        low = mid + 1
    else:
        high = mid - 1
print(high)