import sys

N = int(sys.stdin.readline())

for n in range(N):
    wordList = list(sys.stdin.readline().rstrip().split())
    reverseWords = []

    for word in wordList:
        reverseWords.append(word[::-1])

    result = " ".join(reverseWords)
    print(result)