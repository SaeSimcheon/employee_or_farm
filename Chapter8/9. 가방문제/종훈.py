import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline  # 입력량이 많을 때 입력 속도가 빨라짐
#s = input().rstrip(): # readline 쓰면서 문자열을 읽을 때 문자열 끝에 줄바꿈 기호까지 읽기 때문에 탈피해야함 

################ 동적 계획법 #################

#### 냅색(knapsack) 알고리즘
# 아니 이거 좀 신박하네....


if __name__ == "__main__":
    n, m = map(int, input().split())
    dy = [0] * (m+1) # dy[i] : 가방에 i 무게까지 담을 수 있을 때 보석의 최대가치 입력

    # 나랑 다른 점 : 어차피 하나씩 볼 거니까 굳이 list에 다 안넣고 하나씩 불러서 계산
    for i in range(n):
        w, v = map(int, input().split())
        for j in range(w, m+1):
            dy[j] = max(dy[j], dy[j-w] + v) # dy[j-w] : 그 보석을 넣기 전 무게에서 최대가치
    print(dy[m])
            

'''
# 설명듣고 품, 100점
if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = []
    for _ in range(n):
        a, b = map(int, input().split())
        arr.append((a, b))
    

    dy = [0] * (m+1) # dy[i] : 가방에 i 무게까지 담을 수 있을 때 보석의 최대가치 입력
    for i in range(n):
        w = arr[i][0]
        money = arr[i][1]
        for j in range(w, m+1):
            res = dy[j-w] + money
            if res > dy[j]:
                dy[j] = res
    print(dy[m])
'''
    
