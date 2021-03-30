import sys
#sys.stdin=open("input.txt", "rt")
'''
n,k = map(int, input().split())
a = list(map(int, input().split()))

seq = []
for i in range(n):
    for j in range(i+1,n):
        for l in range(j+1,n):
            summ = a[i]+a[j]+a[l]
            seq.append(summ)
seq.sort(reverse=True)
print(seq[k-1])
'''
n,k = map(int, input().split())
a = list(map(int, input().split()))

res=set() # 중복 제거하는 자료구조

for i in range(n):
    for j in range(i+1,n):
        for m in range(j+1,n):
            res.add(a[i]+a[j]+a[m]) # res는 append가 아니라 add
res = list(res) # res는 list가 아니라 list화 해야함
res.sort(reverse=True)
print(res[k-1])



'''
1. set -> 중복 제거하는 자료구조 / 이걸 몰라서 중복 처리가 안됨
    -> input에서 중복은 별 상관이 없나보다 / output만 중복처리
    -> set 자료구조 익히기(add, not list)
'''
