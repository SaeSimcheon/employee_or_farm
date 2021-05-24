import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline  # 입력량이 많을 때 입력 속도가 빨라짐
#s = input().rstrip(): # readline 쓰면서 문자열을 읽을 때 문자열 끝에 줄바꿈 기호까지 읽기 때문에 탈피해야함 

################ 동적 계획법 #################

#### 냅색(knapsack) 알고리즘


if __name__ == "__main__":
    n, m = map(int, input().split())
    dy = [0] * (m+1) 
    
    for i in range(n):
        ps, pt = map(int, input().split())
        for j in range(m, pt-1, -1): # 중복이 되지 않게 하기 위해 뒤에서부터
            dy[j] = max(dy[j], dy[j-pt] + ps)
    print(dy[m])

    
'''

# 40점.. 뭐가 잘못된건지 모르겠음
if __name__ == "__main__":
    n, m = map(int, input().split())
    dy = [0] * (m+1) 
    
    for i in range(n):
        w, v = map(int, input().split())
        ch = [0]*(m+1)
        ch[v] = 1
        dy[v] = w
        
        for j in range(v, m+1):
            if dy[j-v] != 0 and ch[j-v] == 0:
                if dy[j] < (dy[j-v] + w) :   
                    dy[j] = dy[j-v] + w
                    ch[j] = 1
            elif dy[j-v] == 0 and ch[j-v] == 0:
                dy[j] = w
                ch[j] = 1
                #print(dy)
            
    print(max(dy))
'''
