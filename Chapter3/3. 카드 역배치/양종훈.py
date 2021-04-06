import sys
#sys.stdin = open("input.txt", "rt")

a = list(range(21))
for _ in range(10): # _를 넣으면 변수가 없이 10번 도는 것
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i] # reverse 함수보다 직접 바꿔주는 것을 지향

a.pop(0) # 0번 index있는 값을 삭제
for x in a:
    print(x, end = ' ')


'''
cards = list(range(1,21))

for n in range(10):
    i, j = map(int, input().split())
    #print(i, j)
    i -= 1
    
    cards[i:j] = reversed(cards[i:j])
    #print(cards)

for i in range(20):
    print(cards[i], end = ' ')
'''