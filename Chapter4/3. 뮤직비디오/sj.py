import sys
#sys.stdin = open("input.txt", "rt")
n, m = map(int, input().split())
a = list(map(int, input().split()))

def Count(mag):
    dvdset = []
    setlist = 0
    for i in a:
        setlist += i
        if setlist>mag:
            setlist -= i
            dvdset.append(setlist)
            setlist = 0
            setlist += i
    else:
        dvdset.append(setlist)
    return(len(dvdset))

lt = 1
rt = sum(a)
minimum = 0
while lt<=rt:
    mid = (lt+rt)//2
    if Count(mid)<=m:
        minimum = mid
        rt = mid-1
    else:
        lt = mid+1
print(minimum)
'''
def Count(capacity):
    cnt = 1
    sum = 0
    for x in a:
        if sum+x>capacity:
            cnt+=1
            sum = x
        else:
            sum+=x
    return cnt

maxx = max(a)
lt = 1
rt = sum(a)
res = 0
while lt<=rt:
    mid = (lt+rt)//2
    if mid>=maxx and Count(mid)<=m: # 길이 9인 곡이 무조건 들어가야되기 때문에 답은 9 이상이어야 함.
        res=mid
        rt = mid-1
    else:
        lt = mid+1
print(res)
'''
# 느낀점
# 1. 아직 이분탐색이 익숙치가 않음
# 2. count define할때 저렇게 줄일수 있구나

# 배운점
# 1. if문 간소화/ 조건에 (sum+x) 요런식으로도 가능
# 2. 3장이라는데 dvd 갯수를 최소화해야 한대서 2장도 된다는 점, 즉 '<=m'이고 그때 mid가 답이 될수가 있음
