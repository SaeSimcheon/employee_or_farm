import sys
#sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
lt = 0
rt = n-1

while lt <= rt:
    mid = (lt + rt) // 2
    if a[mid] == m:
        print(mid + 1)
        break
    elif a[mid] > m:
        rt = mid-1
    else:
        lt = mid+1


'''
n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
#a = sorted(a)
#print(a)
for i in range(n):
    if a[i] == m:
        print(i+1)
        break
'''

# sorted vs sort
# a.sort() : 원본 리스트 순서 변화
# sorted(a) : 정렬된 새로운 리스트 반환
# a.sort()는 새로운 복사본을 만들지 않기 때문에 sorted(a) 보다 빠르다.
