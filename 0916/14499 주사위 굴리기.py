from sys import stdin
stdin = open('in.txt','r')
input = stdin.readline

N,M,x,y,K = map(int,input().strip().split(' '))
maps = [list(map(int,input().strip().split(' '))) for _ in range(N)]
num,op,D = {k:0 for k in range(1,7)},{1:6,2:5,3:4,4:3,5:2,6:1},{1:(0,1),2:(0,-1),3:(-1,0),4:(1,0)}
arr = list(map(int,input().strip().split(' ')))
#동쪽은 1, 서쪽은 2, 북쪽은 3, 남쪽은 4
# 1: 4 2:4 3:4 4:4 5:4 6:4
dic = {
    1:{1:4,2:3,3:5,4:2},
    2:{1:4,2:3,3:1,4:6},
    3:{1:1,2:6,3:5,4:2},
    4:{1:6,2:1,3:5,4:2},
    5:{1:4,2:3,3:6,4:1},
    6:{1:4,2:3,3:2,4:5}
}
st = 1
for a in arr:
    # print('st : ',st)
    if 0<=x+D[a][0]<N and 0<=y+D[a][1]<M:
        x+=D[a][0]
        y+=D[a][1]
        st = dic[st][a]
        print(num[op[st]])
        if maps[x][y] == 0:
            maps[x][y] = num[st]
        else:
            num[st] = maps[x][y]
            maps[x][y] = 0
    # print('now: ',st)
    # print('direct : ',a)
    # print(num)
    # for m in maps:
    #     print(m)