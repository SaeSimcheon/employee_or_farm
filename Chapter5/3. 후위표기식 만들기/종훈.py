import sys
#sys.stdin = open("input.txt", "rt")

##### stack 자료구조 활용 #####

a = input()

stack = []
res = ""

for x in a:
    if x.isdecimal():
        res += x
    else:
        if x == "(":
            stack.append(x)

        elif x == '*' or x == '/':
            # 한번만 보게 되는게 아니라 조건이 만족될 때까지 계속 보게 하려면 while문 사용
            while stack and (stack[-1] == '*' or stack[-1] == '/'): # 동일하거나 우선순위에 있는 것 처리
                res += stack.pop() # 출력값을 바로 입력값으로 받기
            stack.append(x)

        elif x =='+' or x == '-':
            while stack and stack[-1] != '(': # stack이 비거나 (를 만나기 전까지는 작동
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop() # ( 를 제거

# 위 for문을 다 돌았는데 stack에 남아있는 기호 처리
while stack:
    res += stack.pop()

print(res)


'''
a = input()

stack = []
res = ""

for i in range(len(a)):
    if a[i] == "(":
        stack.append(a[i])

    elif a[i] == "*" or a[i] == "/":
'''