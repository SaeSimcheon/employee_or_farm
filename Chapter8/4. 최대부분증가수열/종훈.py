import sys
#sys.stdin = open("input.txt", "rt")
input = sys.stdin.readline  # 입력량이 많을 때 입력 속도가 빨라짐
#s = input().rstrip(): # readline 쓰면서 문자열을 읽을 때 문자열 끝에 줄바꿈 기호까지 읽기 때문에 탈피해야함 

################ 동적 계획법 #################

### Bottom-Up 쓰는 것 같음, 메모이제이션 포함

# 리스트 순서대로 각 항목이 부분증가수열의 마지막 항이라 했을 때, 길이를 dy에 입력
# 앞에 항목들 중 작은 수들 중에서 길이가 가장 긴 것의 길이 +1 해준 것을 저장

n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)

dy = [0] * (n+1)
dy[1] = 1

res = 0

for i in range(2, n+1):
    max = 0
    for j in range(i-1, 0, -1): # i-1 부터 1 까지 거꾸로 range
        if arr[j] < arr[i] and dy[j] > max:
            max = dy[j]
    dy[i] = max + 1
    if dy[i] > res:
        res = dy[i]

print(res)


'''
# 설명만 듣고 푼거 100점
n = int(input())
arr = list(map(int, input().split()))

dy = [0] * (n+1)
dy[1] = 1

for i in range(2, n+1):
    for j in range(1,i):
        if arr[j-1] < arr[i-1] and (dy[j]+1) > dy[i]:
            dy[i] = dy[j]+1
    if dy[i] == 0:
        dy[i] = 1
            

print(max(dy))
'''
