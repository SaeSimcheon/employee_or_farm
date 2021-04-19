import sys
#sys.stdin=open("input.txt", "rt")
a = input()
stk = []
eqt = ''
for i in a:
    if i.isdigit():
        eqt += i
    else:
        if i == "(":
            stk.append(i)
        elif i == "*" or i == "/":
            while stk and (stk[-1]=="*" or stk[-1]=="/"):
                eqt += stk.pop()
            stk.append(i)
        elif i == "+" or i == "-":
            while stk and stk[-1]!="(": # stack 맨뒤에 (가 있으면 ()안의 연산자니까 먼저 처리해야함
                eqt += stk.pop()
            stk.append(i)
        elif i == ")":
            while stk and stk[-1]!="(":
                eqt += stk.pop()
            stk.pop()

while stk:
    eqt += stk.pop()
print(eqt)

# 첫시도 100
# 엄청 많은 시행착오
# stack은 last in first out인데 조건이 많이 필요
# 어렵다,,, 2시간 걸린거 같은데

# 연산처리가 우선인 연산자가 stack에 있다면 먼저 처리를 하고 stack에 쌓는식으로
# 빠르지 않다면 바로 stack
# (는 바로 stack )가 나오지 않는 이상 나올일 없음

# 10진수 확인할때 decimal을 쓴다 / 왜? digit은 지수도 인식한대
# 배울점
# 1. 시뮬레이션 우선 / 문제 이해가 시급하다(우선 처리 연산자 구분)
# 2. 스택 개념에 충실한 풀이
