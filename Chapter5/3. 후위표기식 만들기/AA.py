import sys

#sys.stdin=open('input.txt','rt')
'''
middle = input()
stack = list()
answer =''
operator = list()

def is_int(character):
    try:
        int(character)
        return True
    except ValueEror:
        return False


for i in range(len(middle)):
    if is_int(middle[i]):
        answer = answer + middle[i]
    elif middle[i] == '*' :
        answer =answer + middle[i+1])
        answer = answer + middle[i]
    elif middle[i] == '+' :
        stack.append(middle[i])
    elif middle[i] == '/' :
        aswer = answer + middle[i+1]
        aswer = answer + middle[i]
    elif middle[i] == '(':
        stack.append

'''
'''
Stack 문제 해결 시
stack 않에 쌓는 기준은 무엇을 먼저 처리할 것인가에 대한 기준으로
-> 먼저 들어가면 나중에 처리한다는 뜻
'''

a = input()
stack = list()
res = ''
for x in a:
    if x.isdecimal():
        res+=x
    else :
        if x == '(' :
            stack.append(x)
        elif x == '*' or '/':
            while stack and (stack[-1] == '*' or stack[-1]=='/'):
                res += stack.pop()
            stack.append(x)
        elif x =='+' or '-' :
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)
        elif x == ')' :
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()

while stack:
    res+=stack.pop()

print(res)




