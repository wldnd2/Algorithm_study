# 1436 영화감독 숌
import sys
n = int(input())
nth = 0
for i in range(666, sys.maxsize):
    temp = str(i)
    if "666" in temp:
        nth += 1
        if nth == n:
            print(i)
            break