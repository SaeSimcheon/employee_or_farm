'''
알파코드
chr(91) == "a"
chr(92) == "b" ...

'''

import sys
#sys.stdin = open("in2.txt","r")

num = input()
#print(num)
'''
num = '25114'
'''
dic = {str(k):chr(96+k).upper() for k in range(1,27)}

ans = []
def DFS(num,code):
    global ans
    if len(num) == 0:
        if code not in ans:
            ans.append(code)
            print(code)
        return

    else:
        if num[0] in dic.keys():
            DFS(num[1:],code + dic[num[0]])

        if num[0:2] in dic.keys():
            DFS(num[2:],code + dic[num[:2]])

DFS(num,"")
print(len(ans))
