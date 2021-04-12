'''
회의실 배정(그리디) : 그리디 문제는 정렬과 같다라고 함.


1. 같은 시간에 시작하면 끝나는 시점이 빠른 회의 선택
    >> 2번에서 sort하기 때문에 할 필요 없나?(그렇네)
2. 회의 끝나는 시점,시작 시점으로 Sort
3. 시작하는 시점이 빠르면 선택


sort 함수도 key = lambda 가능하네?

sort vs sorted
1. sort : list 만 가능 sorted : 모든 iterable에 가능 (list,tuple,dic,문자열)
2. sort 원본 리스트 순서 변환 sorted 원본 영향 없음
3. sort가 새로운 복사본을 만들지 않아 좀더 빠름.
'''

import sys

#sys.stdin = open("in3.txt","r")

'''
n = 5
arr = [[1,4],[2,3],[3,5],[4,6],[5,7]]
'''

n = int(input())
dic = dict()

for i in range(n):
    k,v = map(int,input().split())

    if k not in dic.keys():
        dic[k] = v
    else:
        if dic[k] > v:
            dic[k] = v
arr = []
for k,v in dic.items():
    arr.append([k,v])
    
arr = sorted(arr, key = lambda x:(x[1],x[0]))

x = -1
ans = 0 
for i in arr:
    if i[0] >= x:
        x = i[1]
        ans += 1

print(ans)


'''
'''
