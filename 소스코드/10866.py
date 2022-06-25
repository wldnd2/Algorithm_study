# 10866 덱
import sys
from collections import deque
input = sys.stdin.readline

d = deque()
for i in range(int(input())):
    command = list(map(str, input().split()))
    if command[0] == "push_front":
        d.appendleft(int(command[1]))
    elif command[0] == "push_back":
        d.append(int(command[1]))
    elif command[0] == "pop_front":
        if len(d):
            print(d.popleft())
        else:
            print(-1)
    elif command[0] == "pop_back":
        if len(d):
            print(d.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(d))
    elif command[0] == "empty":
        if len(d):
            print(0)
        else:
            print(1)
    elif command[0] == "front":
        if len(d):
            print(d[0])
        else:
            print(-1)
    elif command[0] == "back":
        if len(d):
            print(d[-1])
        else:
            print(-1)
