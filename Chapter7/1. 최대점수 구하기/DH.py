'''
최대점수 구하기(DFS)

지금까지 문제 푼 시간 + 한 문제 더 풀 시간 <= 제한시간 >> 풀거나
                                                          안 풀거나
                                           > 제한 시간 >> 못 품

'''
import sys
#sys.stdin = open("in1.txt","r")

n,m = map(int,input().split())

ls_s = []
ls_t = []
for i in range(n):
    x,y = map(int,input().split())
    ls_s += [x]
    ls_t += [y]
#print(ls_s,ls_t)


ans = -10
def F(i,now_t,now_s):
    global ans
    
    if i == n:
        if ans < now_s:
            ans = now_s
        return

    else:
        if ls_t[i] + now_t <= m: 
            F(i+1,now_t,now_s)
            F(i+1,now_t + ls_t[i], now_s + ls_s[i])
        else:
            F(i+1,now_t,now_s)

F(0,0,0)
print(ans)

