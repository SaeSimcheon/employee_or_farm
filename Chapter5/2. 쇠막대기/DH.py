'''
쇠막대기

() : 레이저
(( : 쇠막대기 시작

>> ( : 나오면 뒷자리가 ")" 아닌지 봐서 레이저인지 확인 >> 레이저이면 앞선 "(" 개수만큼 +
                                                          아니면 lt += 1
    ) : 앞에가 "("인지 확인 >> 맞으면 continue
                               아니면 쇠막대기 끝 >> ans +=1 lt -= 1

'''

import sys
'''
sys.stdin = open("in1.txt","r")

n = "()(((()())(())()))(())"
n = "(((()(()()))(())()))(()())"
'''
n = input()
lt = 0
ans = 0
for idx, i in enumerate(n):
    if i == "(":
        if n[idx+1] == ")" :
            ans += lt
        else :
            lt += 1
    else:
        if n[idx-1] == "(":
            continue
        else:
            lt -= 1
            ans += 1
print(ans)
            
