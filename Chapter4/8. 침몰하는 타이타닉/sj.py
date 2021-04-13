import sys
#sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
a = list(map(int,input().split()))
a.sort()
'''boat = 0
while len(a)>=1:
    if a[n-1]+a[0]>m:
        del a[n-1]
        boat+=1
        n-=1
    else:
        del a[n-1],a[0]
        boat+=1
        n-=2
    if len(a)==1:
        a.pop()
        boat+=1
        break
print(boat)'''
# 세번째 시도 100
# 왜 맞는거지????
# 이전까지 풀이는 오름차순으로, 근데 가장 큰사람부터 태우거나, 작은사람부터 태우거나 해서
# 남은 사람중에 들어갈수 있는 사람이 들어가게 했는데 뭔가를 덜 고려한거 같아서 안되더라
# 세번째부터는 접근을 조금 달리해서, max+min 조합으로 들어가고 안들어가고를 따졌는데
# 이게 맞네
cnt = 0
while a: # p가 비어있지 않으면 True, 비어있으면 False
    if len(p)==1:
        cnt+=1
        break
    if a[0]+a[-1]>m: # 리스트 맨마지막은 [-1]로도 접근 가능 n을 굳이 안빼도 된다
        p.pop()
        cnt+=1
    else:
        p.pop(0) # 0을 넣으면 맨 앞자료가 빠진다
        p.pop()
        cnt+=1
print(cnt)

# 느낀점
# 1. 설명을 들으니까 조금 이해가 된다 / 설명 같이 잘듣자
# 2. 난 del을 썼는데, pop이랑 무슨 차이일까

# 배운점
# 1. while 조건에 리스트를 넣으면 비어있으면 False로 받아들인다
# 2. 리스트 맨마지막은 [-1]로도 접근가능 / 굳이 n을 안빼도 된다
# 3. pop(0)도 가능하다
# 4. deque 자료형
# list.pop(0)은 뒤의 자료가 앞으로 이동해서 비효울적
# deque는 앞/뒤에서 뻈다 넣었다 할수 있음 / list와 달리 pop으로 빠져도 앞으로 이동 안함
# 5. 마지막 한명 남는 경우도 고려해야 한다

from collections import deque
a=deque(a)
cnt=0
while a: # p가 비어있지 않으면 True, 비어있으면 False
    if len(p)==1:
        cnt+=1
        break
    if a[0]+a[-1]>m: # 리스트 맨마지막은 [-1]로도 접근 가능 n을 굳이 안빼도 된다
        p.pop()
        cnt+=1
    else:
        p.popleft # deque에서 맨앞에 뺄 때 쓸 수 있는 방법
        p.pop()
        cnt+=1
print(cnt)