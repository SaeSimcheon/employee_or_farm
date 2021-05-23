import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline  # 입력량이 많을 때 입력 속도가 빨라짐
#s = input().rstrip(): # readline 쓰면서 문자열을 읽을 때 문자열 끝에 줄바꿈 기호까지 읽기 때문에 탈피해야함 

################ 동적 계획법 #################

### Bottom-Up 사용, 메모이제이션 포함

if __name__ == "__main__":
    n = int(input())
    bricks = []
    for i in range(n):
        a, b, c = map(int, input().split())
        bricks.append((a, b, c))
    bricks.sort(reverse=True)

    dy = [0]*n
    dy[0] = bricks[0][1]
    res = bricks[0][1]

    for i in range(1, n):
        max_h = 0
        for j in range(i-1, -1, -1): # i-1 번째 벽돌부터 0번째 까지 역순
            if bricks[j][2] > bricks[i][2] and dy[j] > max_h:
                max_h = dy[j]
        dy[i] = max_h + bricks[i][1]
        res = max(res, dy[i])
    print(res)




'''
### 설명듣고 코딩, 100점
n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key = lambda x : (x[0], x[1], [2]), reverse = True)



dy = [0] * n
dy[0] = arr[0][1]
res = 0

for i in range(1, n):
    max = 0
    for j in range(0, i): 
        if arr[j][2] > arr[i][2] and dy[j] > max:
            max = dy[j] 
    if max == 0:
        dy[i] = arr[i][1]
    else:
        dy[i] = max + arr[i][1]
        
    #dy[i] = max
    if dy[i] > res:
        res = dy[i]
print(res)
'''

