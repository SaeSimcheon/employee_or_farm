import sys
#sys.stdin = open("input.txt", "rt")
n = int(input())
a = list(map(int,input().split()))
'''seq = [0]
chrseq = []
while len(a)>=1:
    if (a[0]<a[n-1] and a[0]>max(seq)):
        seq.append(a[0])
        del a[0]
        n-=1
        chrseq.append("L")
    elif a[0]>a[n-1] and a[n-1]>max(seq):
        seq.append(a[n-1])
        del a[n-1]
        n-=1
        chrseq.append("R")
    elif a[0]>a[n-1] and a[0]>max(seq):
        seq.append(a[0])
        del a[0]
        n-=1
        chrseq.append("L")
    elif a[0]<a[n-1] and a[n-1]>max(seq):
        seq.append(a[n-1])
        del a[n-1]
        n-=1
        chrseq.append("R")
    else:
        break
    if len(a)==1:
        if a[0]>max(seq):
            seq.append(a[0])
            a.pop()
            chrseq.append("L")
            break
        else:
            a.pop()

seq.pop(0)
print(len(seq))
for i in chrseq:
    print(i, end='')'''

# 두번째 시도 100 / 어거지로 풀었다

# lt와 rt를 양끝단으로 해서, 이분탐색처럼 step마다 lt/rt 변경

lt = 0
rt = n-1
last = 0
res = "" # 문자열 초기화는 이렇게
tmp = []
while lt<=rt:
    if a[lt]>last:
        tmp.append((a[lt], 'L')) # tuple로 넣는다
    if a[rt]>last:
        tmp.append((a[rt], 'R'))
    tmp.sort()
    if len(tmp)==0:
        break
    else:
        res=res+tmp[0][1]
        last=tmp[0][0]
        if tmp[0][1]=='L':
            lt+=1
        else:
            rt-=1
    tmp.clear()
print(len(res)) # 문자열 길이를 재도 ㅇㅋ
print(res)

# 느낀점
# 1. 여기서도 범위로 풀수 있음
# 2. 너무 어렵다 다시 풀라고해도 저렇게 못풀듯
# 3. 답이 문자열 길이는 재는거도 되네

# 배운점
# 1. 빈 값을 만들고 비교(tmp, last)
# 단순히 양끝값을 비교하는게 아니라, 가져온 값을 다시 저장해둬서 비교하면 편리
# 2. 증가수열을 만드는 문제라고 해서 무조건 만들지 않아도 문제를 풀 수 있다
# 문자열만 만들어도 답을 만들수는 있으니까...
