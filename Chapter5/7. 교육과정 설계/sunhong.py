import sys
#sys.stdin=open('in3.txt','r')
a=sys.stdin.readline().split()[0]
n=int(sys.stdin.readline())    

for i in range(n):
    order=[]
    course=sys.stdin.readline().split()[0]
    for x in a:
        try:
            order.append(course.index(x))
        except ValueError:
            break             
    if len(a)==len(order) and order==sorted(order):
        print("#{} YES".format(i+1))
    else:
        print("#{} NO".format(i+1))

## order: [수업설계.index(v) for v in 필수과목]
## 제대로 설계했다면 order==sorted(order) => yes
