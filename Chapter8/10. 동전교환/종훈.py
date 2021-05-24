import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline  # 입력량이 많을 때 입력 속도가 빨라짐
#s = input().rstrip(): # readline 쓰면서 문자열을 읽을 때 문자열 끝에 줄바꿈 기호까지 읽기 때문에 탈피해야함 

################ 동적 계획법 #################

#### 냅색(knapsack) 알고리즘

if __name__ == "__main__":
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())
    
    dy = [1000] * (m+1) # min계산을 위해 큰 숫자로 설정
    dy[0] = 0
    
    for i in range(n):
        for j in range(coin[i], m+1):
            dy[j] = min(dy[j], dy[j - coin[i]] + 1)
    print(dy[m])


'''
# 100점 이긴 한데 뭐지 이 찝찝한 기분은...
if __name__ == "__main__":
    n = int(input())
    money = list(map(int, input().split()))
    m = int(input())
    
    dy = [0] * (m+1)
    
    for i in range(n):
        w = money[i]
        for j in range(w, m+1): # 앞문제와 다르게 max 가 아니라 min을 사용해야 돼서 조건이 달림
            if dy[j-w] == 0: # 앞에 있는게 0이 되면 무조건 0이 min이 되는 것 방지
                dy[j] = 1
            elif dy[j] == 0: # 원래 있는게 0이면 무조건 0이 min이 되는 것 방지
                dy[j] = dy[j-w] + 1
            else: # 전에 세어놓은 개수와 새로 세는 개수 중 적은 것
                dy[j] = min(dy[j], dy[j-w]+1)
    print(dy[m])
'''

