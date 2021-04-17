'''
가장 큰 수

n : 수
m : 제거 가능한 개수

한 자리씩 받으면서 진행

받은 자리가 앞자리 보다 클 경우 몇 번째까지 큰지 개수 세기
    ex : 앞 수 : 5534 받은 수 : 9 >> cnt : 4

    cnt가 m보다 작을 경우 cnt 만큼 지우고 push
                큰 경우 m 만큼 지우고 push

else: push

'''
import sys
#sys.stdin = open("in1.txt","r")

n, m = input().split()
'''

n, m = "9977252641", "5"
'''
n = [int(x) for x in list(n)]
m = int(m)


ans = [n[0]]

for idx,i in enumerate(n[1:]):
    if i > ans[-1] :
        cnt = 0
        for nn in ans[::-1]:
            if i > nn :
                cnt += 1
            else :
                break

        if m >= cnt:
            m -= cnt
            ans = ans[:-cnt] + [i]
        else:
            ans = ans[:-m] + [i]
            m = 0
    else:
        ans += [i]

    if m == 0:
        break
if m != 0:
    ans = ans[:-1*m]
if idx == 0:
    ans = [str(x) for x in ans]
    print("".join(ans))
else:
    ans += n[idx+2:]
    ans = [str(x) for x in ans]
    print("".join(ans))


