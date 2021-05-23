# dynamic programming
'''
작은 단위로 큰 문제를 축소시키는,,
가장 작은 단위 문제 -> 그다음 단위 문제 -> .... 문제를 점점 키워나간다
가장 작은건 직관적으로 바로 해결할 수 있는, 점화식과 유사한 형태
Bottom-Up (문제의 크기를 확장시키기)
'''
'''
import sys
sys.stdin = open("input.txt", 'r')
n = int(input())
dy = [0]*(n+1)
dy[1] = 1
dy[2] = 2
for i in range(3,n+1):
    dy[i] = dy[i-2] + dy[i-1]
print(dy[n])'''

'''
Top-Down : 재귀, 메모이제이션
DFS를 사용, level을 하나씩 줄이면서 방법의 수를 더하는 식으로
기존에 구해진 값은 기록하는 식으로
'''
import sys
sys.stdin = open("input.txt",'r')
def DFS(len):
    if dy[len]>0:
        return dy[len]
    if len==1 or len==2:
        return len
    else:
        dy[len]=DFS(len-1)+DFS(len-2)
        return dy[len]

if __name__=="__main__":
    n = int(input())
    dy = [0]*(n+1)
    print(DFS(n))
