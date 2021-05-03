'''
합이 같은 부분집합(DFS : 아마존 인터뷰)

{1, 3, 5, 7},{6, 10}
{6, 10},{1, 3, 5, 7}

이렇게 중복되는걸 잡을 방법 생각 >> 한번 Yes >> 전부 return
'''

import sys

#sys.stdin = open("in1.txt","r")

n = int(input())
ll = list(map(int,input().split()))
'''

n = 6
ll = [1,3,5,6,7,10]
'''

L_ll = []
R_ll = []


ans = "NO"
def DFS(ll,L_ll,R_ll):
    global ans
    if len(ll) == 0:
        if sum(L_ll) == sum(R_ll):
            ans = "YES"
        return
    elif ans == "YES":
        return

    else:
        temp = ll[0]
        DFS(ll[1:],L_ll+[temp],R_ll)
        DFS(ll[1:],L_ll,R_ll+[temp])        
DFS(ll,L_ll,R_ll)

print(ans)
'''    


def DFS(ll,L_ll,R_ll):
    global RE
    if RE == "Yes":
        return

    if len(ll) == 0:
#        print(L_ll)
        if sum(L_ll) == sum(R_ll):
            RE = "YES"
    else:
        temp = ll[0]
        DFS(ll[1:],L_ll+[temp],R_ll)
        DFS(ll[1:],L_ll,R_ll+[temp])
            
DFS(ll,L_ll,R_ll)
print(RE)
'''
