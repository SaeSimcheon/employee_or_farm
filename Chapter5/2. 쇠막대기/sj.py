import sys
#sys.stdin=open("input.txt", "rt")
'''a = input()
stack = []
stick = 0
for i in range(len(a)):
    if a[i] == "(":
        stack.append(a[i])
    else:
        stack.pop()
        if a[i-1]=="(":
            stick+=len(stack)
        else:
            stick+=1
print(stick)

'''
# 문제 감을 못잡겠어서 강의 초반 설명보고 풀었음

# (는 stack, )는 pop / ) 나올때마다 이전에 (이면 stack 길이만큼 더하기
# 이전에 )면 +1 씩 카운트

# 배운점
# 1. 문제 풀기전에 시뮬레이션 해보자
