import sys

N = int(sys.stdin.readline())

stack = []
def Push(cmd):
    value = cmd.split(' ')[1].rstrip('\n')
    stack.append(value)

def Pop(cmd):
    if len(stack) != 0:
        print(stack[-1])
        stack.pop(-1)
    else:
        print(-1)

def Size(cmd):
    print(len(stack))

def Empty(cmd):
    if len(stack) == 0:
        print(1)
    else:
        print(0)

def Top(cmd):
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])

for n in range(N):
    command = sys.stdin.readline()

    if "push" in command:
        Push(command)
    if "pop" in command:
        Pop(command)
    if "size" in command:
        Size(command)
    if "empty" in command:
        Empty(command)
    if "top" in command:
        Top(command)