'''
후위표기식 만들기

설명;;;

숫자 : 무조건 ans
기호 : ( >> 무조건 stack
       -,+ : 2 *,/ :3
       stack에 마지막 기호의 level이 tmp level 보다 높거나 같으면 >> pop 마지막에 tmp push
                                                                     아니면 push
        ) : ( 가 나올 때까지 pop

        전부다 읽으면 계속 pop
'''
import sys


n = input()
#n = "3+5*2/(7-2)"
#n = "3*(5+2)-9"
n = list(n)
dic = {"(" : 1,
       "-" : 2,"+" : 2,
       "*" : 3,"/" : 3}

stack = []
ans = ""
while n:
    tmp = n.pop(0)

    if tmp.isdigit():
        ans += tmp

    else:
        if len(stack) == 0:
            stack.append(tmp)
        elif tmp == ")":
            while stack:
                aa = stack.pop()
                if aa =="(":
                    break
                else:
                    ans += aa
        elif tmp == "(":
            stack.append(tmp)
        elif dic[stack[-1]] >= dic[tmp]:
            while stack:
                if dic[stack[-1]] >= dic[tmp]:
                    ans += stack.pop()
                else:
                    break
            stack.append(tmp)
        elif dic[stack[-1]] < dic[tmp]:
            stack.append(tmp)
#    print(ans,stack,tmp)
print(ans + "".join(stack[::-1]))
