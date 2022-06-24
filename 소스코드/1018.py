# 1018 체스판 다시 칠하기
import sys
input = sys.stdin.readline

chess = []
n, m = map(int, input().split())
for i in range(n):
    chess.append(input())

result = []
chessA = ["BWBWBWBW", "WBWBWBWB"]
chessB = ["WBWBWBWB", "BWBWBWBW"]

for i in range(n-8+1):
    for j in range(m-8+1):
        temp = [row[j:j+8]for row in chess[i:i+8]]
        cntA, cntB = 0, 0
        for k in range(len(temp)):
            # chessA와 chessB 전부를 다 비교해서 최소 값을 찾는다.
            for index in range(len(temp[k])):
                if chessA[k % 2][index] != temp[k][index]:
                    cntA += 1
            for index in range(len(temp[k])):
                if chessB[k % 2][index] != temp[k][index]:
                    cntB += 1
        # 둘 중 최소값만을 append한다.
        result.append(min(cntA, cntB))
print(min(result))
