'''
가장 높은 탑 쌓기
'''
'''
n = 5
arr = [[25,3,4],
       [4,4,6],
       [9,2,3],
       [16,2,5],
       [1,5,2]] #넓이,높이,무게

벽돌 순서대로 쌓을 필요 없음
'''
import sys
#sys.stdin = open("in2.txt")


n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

arr.sort(key = lambda x: (-x[0],-x[2]))
dy = [arr[0]]

ans = -1
for ls in arr[1:]:
    tmp_h = 0

    for dyy in dy:
        if dyy[0] > ls[0] and dyy[2] > ls[2]:
            if tmp_h < dyy[1]:
                tmp_h = dyy[1]

    dy.append([ls[0],tmp_h + ls[1], ls[2]])

    if ans < dy[-1][1]:
        ans = dy[-1][1]

print(ans)

