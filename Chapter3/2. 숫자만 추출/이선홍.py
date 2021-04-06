import sys
import string
#sys.stdin=open("c:/Users/jung/Desktop/AA/in1.txt","r")
dat=input()
alphabet_list=list(string.ascii_lowercase) # alphabet list, containing [a~z]
nat_num='0'
for x in dat:
    if x.lower() not in alphabet_list:
        nat_num+=x

nat_num=int(nat_num)
ali_num=0

for i in range(1,nat_num+1):
    if nat_num%i==0:
        ali_num+=1

print(nat_num)
print(ali_num)
