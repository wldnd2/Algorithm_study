# 11650 좌표 정렬하기
import sys
input = sys.stdin.readline
all = []

for i in range(int(input())):
    x, y = map(int, input().split())
    all.append([x, y])

all.sort()
for i in range(len(all)):
    print(*all[i])
