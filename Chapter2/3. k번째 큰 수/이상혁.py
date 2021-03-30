from itertools import combinations
import sys
sys.stdin = open("cht2_3_input.txt","rt")



n,k= map(int,input().split())
a=list(map(int,input().split()))

comb=list(combinations(a,3))
comb_sum=list(map(sum,comb))
comb_sum=list(set(comb_sum))
comb_sum.sort(reverse= True)
print(comb_sum[k-1])