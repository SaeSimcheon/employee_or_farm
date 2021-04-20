import sys

sys.stdin = open("input.txt","rt")

seq = input()
seq=list(seq)

print(seq)

stack  = []
out = 0
for idx, value in enumerate(seq):
    print(idx,stack,out)
    if value =="(":
        stack.append(value)
    else:
        if previous =="(":
            stack.pop()
            out += len(stack)
        else:
            stack.pop()
            out += 1
    previous = value
    
print(out)