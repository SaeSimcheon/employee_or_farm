import sys
sys.stdin=open("input.txt", "r")
N,M = map(int,input().split())
seq = list(map(int,input().split()))

#print(N,M,seq)


names_patient=list(range(0,N))
i = 0
while seq :
    patient=seq.pop(0)
    name = names_patient.pop(0)
    if  patient < max(seq):
        seq.append(patient)
        names_patient.append(name)
    else:
        if name == M:
            i+=1
            break
        else:
            i+=1
            continue
print(i)