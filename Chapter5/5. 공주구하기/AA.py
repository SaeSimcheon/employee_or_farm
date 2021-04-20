import sys

#sys.stdin=open('input.txt','rt')

last = input()

stack = list()

answer = ''
for x in last:
    if x.isdecimal() :
        stack.append(int(x))
    if not x.isdecimal() :
        if x == '+':
            numb1 = int(stack[-2])
            numb2 = int(stack[-1])
            ans = numb1 + numb2
            stack.pop()
            stack.pop()
            stack.append(ans)
        if x == '-':
            numb1 = int(stack[-2])
            numb2 = int(stack[-1])
            ans = numb1 - numb2
            stack.pop()
            stack.pop()
            stack.append(ans)
        if x == '*':
            numb1 = int(stack[-2])
            numb2 = int(stack[-1])
            ans = numb1 * numb2
            stack.pop()
            stack.pop()
            stack.append(ans)
        if x == '/':
            numb1 = int(stack[-2])
            numb2 = int(stack[-1])
            ans = numb1 / numb2
            stack.pop()
            stack.pop()
            stack.append(ans)

print(stack[0])
