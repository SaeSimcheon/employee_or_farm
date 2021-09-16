import sys
sys.stdin=open("input.txt", "r")
n = int(input())
A = list(map(int, input().split()))
b, c = map(int, input().split())
ans = 0
for a in A:
    if a <= b:
        ans += 1
    else:
        a -= b; ans += 1
        r, k = divmod(a, c)
        if k > 0:
            ans += r+1
        else:
            ans += r
print(ans)