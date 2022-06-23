# 10816 숫자 카드 2
import sys
input = sys.stdin.readline

dic = {}

n, data = int(input()), sorted(list(map(int, input().split())))
input()
card = list(map(int, input().split()))
for i in data:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

# 다른 사람의 출력 방식
print(' '.join(str(dic[n]) if n in dic else '0' for n in card))

# 내가 한 출력 방식
# for i in card:
#     if i in dic:
#         print(dic[i], end=" ")
#     else:
#         print(0, end=" ")
