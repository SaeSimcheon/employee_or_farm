import sys

sys.stdin = open("input.txt","rt")

seq = input()
seq=list(seq)




stack = list()
previous = None

for idx , value in seq:
    
    front=seq.pop(0)
    if front not in ["+" , "-", "*", "/", "(", ")"]:
        if previous in ["+", "-", "*", "/", "(", ")"] :
            
        else :
            
    else:
        
     
    previous = front