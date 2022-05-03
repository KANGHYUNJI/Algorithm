import sys

N = int(sys.stdin.readline())

now = 0
stackList = []
resultList = []
check = True

for n in range(N):
    num = int(sys.stdin.readline())

    while now < num:
        now += 1
        stackList.append(now)
        resultList.append("+")

    if stackList[-1] == num:
        stackList.pop()
        resultList.append("-")
    else:
        check = False
        break

if check == False:
    print("NO")
else:
    for i in resultList:
        print(i)


