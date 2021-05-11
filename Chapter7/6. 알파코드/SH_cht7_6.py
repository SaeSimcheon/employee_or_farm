import sys

sys.stdin = open("input.txt","rt")

code= input()


asc=list(range(ord("A") , ord("Z")+1))
eng=[chr(i) for i in asc]
eng.insert(0,"0")
#print(eng)

out = list()
#print(len(code))
def DFS(L,string,indicator):
  #  print(L)
  #  print(L,indicator)
    if L > len(code):
        return
    if indicator == 0:
        out.append(string)
    else:
        if code[L] =="0":
            return
        
        if code[L] =="1":
            if indicator >=2:
                DFS(L+1,string+eng[int(code[L])],indicator-1)
                DFS(L+2,string+eng[int(code[L:(L+2)])],indicator-2)    
            else :
                DFS(L+1,string+eng[int(code[L])],indicator-1)
        elif code[L] == "2":
            
            if indicator >=2:
                if int(code[L+1]) > 6 :
                    DFS(L+1,string+eng[int(code[L])],indicator-1)
                else :
                    DFS(L+1,string+eng[int(code[L])],indicator-1)
                    DFS(L+2,string+eng[int(code[L:(L+2)])],indicator-2)                
            else:
                DFS(L+1,string+eng[int(code[L])],indicator-1)
                
        else :
            DFS(L+1,string+eng[int(code[L])],indicator-1)
            
            
DFS(0,"",len(code))
out.sort()

for i in out:
    print(i)
print(len(out))