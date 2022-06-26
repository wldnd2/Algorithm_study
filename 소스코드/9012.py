# 9012 괄호
import sys
input = sys.stdin.readline

stack = []
for _ in range(int(input())):
    check = True
    str1 = list(input().rstrip())
    for i in str1:
        if i == '(':
            stack.append(i)
        else:
            if len(stack) == 0:
                check = False
                break
            stack.pop()
    if check and len(stack) == 0:
        print("YES")
    else:
        print("NO")
    stack.clear()
