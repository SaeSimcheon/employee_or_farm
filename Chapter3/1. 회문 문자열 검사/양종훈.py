import sys
#sys.stdin = open("input.txt", "rt")

n = int(input())

for i in range(n):
    s = input()
    s = s.upper()
    size=len(s)
    for j in range(size//2):
        if s[j] != s[-1-j]:
            print("#%d NO" % (i+1))
            break
    else:
        print("#%d YES" % (i+1))

'''
for i in range(n):
    word = input()
    word = word.lower()
    word2 = word[::-1]
    
    if word2 == word:
        print("#%d YES" % (i+1))
    else:
        print("#%d NO" % (i+1))
'''