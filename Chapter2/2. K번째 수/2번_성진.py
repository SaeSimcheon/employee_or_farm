import sys
#sys.stdin=open("input.txt", "rt")

T = int(input())
for t in range(T):
    n, s, e, k=map(int, input().split())
    a=list(map(int, input().split()))
    a=a[s-1:e]
    a.sort()
    print("#%d %d" %(t+1, a[k-1]))


'''
1. 데이터 불러오는거 문제 : 여러 줄이 있을 때 input으로 불러오는걸 몰랐네
2. list slice가 어떻게 되는지....
3. list 차순 정렬은 list.sort()
4. print에도 형식이 있다. "#%d %d" %(t+1, a[k-1])
    -> %d와 뒤의 %()가 대응되는 형식
'''
