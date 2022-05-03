import sys

N, K = map(int, sys.stdin.readline().split())

peopleList = [i for i in range(1,N+1)]
resultList = []
cnt = 0

while len(peopleList) != 0:
    cnt = (cnt + (K-1)) % len(peopleList)
    popValue = peopleList.pop(cnt)
    resultList.append((str(popValue)))

print("<" + ', '.join(resultList) + ">")
