'''
재귀함수를 이용한 이진수 출력
'''

n = int(input())

#n = 11

def Len(n):
    i = 0
    while 1:
        if n <= 2**i:
            break
        else: i += 1
    return i

def Make(n,Len):

    if Len == 1:
        return str(n)

    else:

        if n - 2 **(Len-1) >= 0:
            n -= 2 **(Len-1)
#            Temp = "1"
            return "1" + Make(n,Len-1)
        else:
#            Temp = "0"
            return "0" + Make(n,Len-1)
#        Len -= 1
#        print(Temp,end = "")        
#    return Temp + Make(n,Len)

print(Make(n,Len(n)))
