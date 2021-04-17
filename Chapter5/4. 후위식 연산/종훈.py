import sys
#sys.stdin = open("input.txt", "rt")

##### stack 자료구조 활용 #####

a = input()

stack = []

for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x == '+':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 + n1)
        elif x == '-':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 - n1)
        elif x == '*':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 * n1)
        elif x == '/':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 / n1)
print(stack[0])


'''
a = input()

stack = []

for x in a:
    if x.isdecimal():
        stack.append(int(x))
    elif x == "+":
        b = int(stack.pop())
        c = int(stack.pop())
        stack.append(c + b)
    elif x == "-":
        b = int(stack.pop())
        c = int(stack.pop())
        stack.append(c - b)
    elif x == "*":
        b = int(stack.pop())
        c = int(stack.pop())
        stack.append(c * b)
    elif x == "/":
        b = int(stack.pop())
        c = int(stack.pop())
        stack.append(c / b)
print(stack[0])
'''