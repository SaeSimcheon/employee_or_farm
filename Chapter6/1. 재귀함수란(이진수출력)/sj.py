import sys
#sys.stdin=open("input.txt", "rt")
'''def DFS(x):
    if x>0:
        a = x%2
        x = x//2
        DFS(x)
        print(a, end='')
if __name__=="__main__":
    n = int(input())
    DFS(n)'''

# 첫 시도 100
# 처음 선수강의에서 설명한 개념처럼 구현
# 왜맞지? 싶지만 맞는거 같기도하고
def DFS(x):
    if x==0:
        return # 그냥 return은 함수를 종료
    else:
        DFS(x//2)
        print(x%2, end='')

if __name__=="__main__":
    n = int(input())
    DFS(n)