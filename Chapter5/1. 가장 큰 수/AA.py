import sys

#sys.stdin=open('input.txt','rt')

n, m = input().split()
m = int(m)
answer = ''
while m > 0:
    max_value = max(n[0:-m])
    answer = answer + str(max_value)
    max_index = n.index(max_value)
    n = n[max_index+1:]
    m -= 1

print(answer)

