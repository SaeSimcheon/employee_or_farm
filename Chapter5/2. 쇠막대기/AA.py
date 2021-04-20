import sys

#sys.stdin=open('input.txt','rt')

steel = input()
sum = 0
stack = list()

for i in range(len(steel)):
    if steel[i] == '(':
        stack.append(steel[i])
    elif steel[i] == ')':
        if steel[i-1] == '(' :
            stack.pop()
            sum += len(stack)
        else :
            stack.pop()
            sum += 1
    
print(sum)

