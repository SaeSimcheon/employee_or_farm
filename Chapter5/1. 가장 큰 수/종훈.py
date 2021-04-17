import sys
#sys.stdin = open("input.txt", "rt")

# 앞에서부터 하나씩 체크하는데 앞에서 자기 자신보다 작은 숫자가 있으면 지우고 자기가 앞으로 가는데 지우는 개수는 m개
# 이런 것을 자연스럽게 쉽게 코드로 구현할 수 있는 자료구조가 stack

####### stack #########
# Last in, First out 구조
# 들어가는 입구와 나오는 출구가 한 곳인 구조
# 제일 먼저 들어간게 나중에 나옴
# list를 이용해서 append로 in, pop으로 out

num, m = map(int, input().split())

num = list(map(int, str(num)))

stack = []
for x in num:
    while stack and m > 0 and stack[-1] < x: # while문에 list가 들어가면 비어있으면 False, 값이 있으면 True
        stack.pop()
        m -= 1
    stack.append(x)

if m != 0:
    stack = stack[:-m]

res = ''.join(map(str, stack))
print(res)




'''
num, m = map(int, input().split())
num = str(num)
num_list = []

for i in range(len(num)):
    num_list.append(int(num[i]))
#print(num_list)
#print(num_list[0:-0])
res = ""
idx = 0
rt = len(num_list) - m
while True:
    
    lst = num_list[idx : rt]
    mx = max(lst)
    print(mx)
    res = res + str(mx)

    idx = num_list.index(mx)
    rt += 1
    if rt > len(num_list):
        break
print(res)
'''