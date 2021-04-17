'''
단어 찾기
Counter쓰면 더 편할듯?

'''
#import sys
from collections import Counter
#word = list("AbaAeCe")
word = list(input())
dic1 = Counter(word)

#word = "baeeACA"
word = list(input())
dic2 = Counter(word)


if len(dic2-dic1) == 0:
    print("YES")
else :
    print("NO")
'''
#sys.stdin = open("in1.txt","r")

#word = "AbaAeCe"
word = input()
dic1 = {}

for i in word:
    if i not in dic1.keys():
        dic1[i] = 1
    else :
        dic1[i] +=1

#word = "baeeACA"
word = input()
dic2 = {}

for i in word:
    if i not in dic2.keys():
        dic2[i] = 1
    else :
        dic2[i] +=1

for k,v in dic1.items():
    if k not in dic2.keys():
        print("NO")
        break

    else:
        if dic2[k] != v:
            print("NO")
            break
else:
    print("YES")
'''
