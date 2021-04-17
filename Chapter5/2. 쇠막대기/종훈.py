import sys
#sys.stdin = open("input.txt", "rt")

##### stack 자료구조 활용 #####

# ( 가 오면 stack에 쌓고 ) 가 왔을 때, 앞이 ( 이면 앞에 (을 포함해서 제거한 후 앞쪽에 남은 (의 개수를 더한다.

s = input()
stack = []
cnt = 0

for i in range(len(s)):
    if s[i] =="(":
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1] == "(":
            cnt += len(stack)
        else:
            cnt += 1
print(cnt)


# 알고리즘 생각 안나서 설명듣고 코드만 내가 짜봄

'''
a = list(input())
#print(a)

stick = []
cnt = 0
for i in range(len(a)):
    if a[i] == "(":
        stick.append(a[i])
    elif a[i] == ")" and a[i-1] == "(":
        stick.pop()
        cnt += len(stick)
    else:
        stick.pop()
        cnt += 1
print(cnt)
'''

