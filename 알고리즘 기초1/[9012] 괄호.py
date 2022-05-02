import sys

T = int(sys.stdin.readline())

for t in range(T):
    words = sys.stdin.readline()

    cnt = 0
    check = True
    for word in words:
        if word == '(':
           cnt += 1
        if word == ')':
            cnt += -1
        if cnt < 0:
            check = False
            break
    if check == False or cnt != 0:
        print("NO")
    else:
        print("YES")
