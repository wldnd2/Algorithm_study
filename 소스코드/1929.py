# 1929 소수 구하기

n, m = map(int, input().split())
m += 1
a = [True] * (m)
last = int(m**0.5)

for i in range(2, last + 1):
    if a[i] == True:
        for j in range(i + i, m, i):
            a[j] = False

for index in range(n, m):
    if index > 1 and a[index]:
        print(index)
