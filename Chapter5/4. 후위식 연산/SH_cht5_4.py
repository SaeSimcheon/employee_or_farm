import sys
sys.stdin=open("input.txt", "r")
seq = input()
seq= list(seq)
print(seq)

stack  =list()
for i in seq:
    if i.isnumeric():
        stack.append(i)
    else:
        print(stack)
        p2= stack.pop()
        p1= stack.pop()
        print(stack)
        if i == "+":
            stack.append(int(p1)+int(p2))
        elif i == "-":
            stack.append(int(p1)-int(p2))
        elif i == "/":
            stack.append(int(p1)/int(p2))
        elif i == "*":
            stack.append(int(p1)*int(p2))

print(*stack)