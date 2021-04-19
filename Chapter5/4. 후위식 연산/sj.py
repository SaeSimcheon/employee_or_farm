import sys
#sys.stdin=open("input.txt", "rt")
eq = input()
stk = []
answer = 0
for i in eq:
    if i.isdigit():
        stk.append(int(i))
        #print(stk)
    else:
        if i == "+":
            a = stk.pop()
            b = stk.pop()
            stk.append(a+b)
            #print(stk)
        elif i == "-":
            a = stk.pop()
            b = stk.pop()
            stk.append(b-a)
            #print(stk)
        elif i == "*":
            a = stk.pop()
            b = stk.pop()
            stk.append(a*b)
            #print(stk)
        elif i == "/":
            a = stk.pop()
            b = stk.pop()
            stk.append(b/a)
            #print(stk)
print(stk[0])

#첫 시도 100
# 앞에보다 상대적으로 간단
# 후위식은 그냥 앞에서부터 계산하면 되는데
# 계산한거를 다시 저장하고~ 반복

