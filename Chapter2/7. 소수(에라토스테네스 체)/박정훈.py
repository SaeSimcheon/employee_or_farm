import sys

#sys.stdin=open('input.txt','rt')

n = int(input())

numbers = list(range(1,n+1))


def chae(lists):
    for i in range(2,n+1):
        numb = lists[i]
        if i == 1:
            pass
        elif lists[i]%numb == 0 :
            for j in range(i, n+1, i) :
                del list[list.index(list[j])]
                lists.remove(lists[j])
            return chae(lists)

print(len(chae(numbers)))
'''


import sys
#sys.stdin= open('input.txt','r')
n = int(input())
ch = [0]*(n+1)
cnt = 0
for i in range(2,n+1):
    if ch[i]==0:
        cnt+=1
        for j in range(i, n+1,i):
            ch[j]=1
print(cnt)
'''

'''
import sys

#sys.stdin=open('input.txt','rt')

n = int(input())

lis = list(range(1,n+1))



def chae(ll,n):
    if n == len(ll):
        return ll

    temp = ll[n]
    temp_ll = ll[:n+1]
    for i in ll[n+1:]:
        if i % temp != 0:
            temp_ll.append(i)

    return chae(temp_ll,n+1)


print(chae(lis,1))
'''
