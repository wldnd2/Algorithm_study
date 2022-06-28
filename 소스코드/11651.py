# 11651 좌표 정렬하기 2
import sys
input = sys.stdin.readline

result = sorted([list(map(int, input().split())) for i in range(int(input()))])
result.sort(key=lambda x: x[1])
for i in result:
    print(*i)
