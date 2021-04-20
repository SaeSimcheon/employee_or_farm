import sys
sys.stdin=open("input.txt", "r")
seq1 = input()
seq2 = input()

seq1_dict = {}
for i in seq1:
    seq1_dict[i] = seq1.count(i)
    


seq2_dict = {}
for i in seq2:
    seq2_dict[i] = seq2.count(i)
    


if seq1_dict == seq2_dict :
    print("YES")
else:
    print("NO")