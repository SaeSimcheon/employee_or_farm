import sys
sys.stdin = open("cht2_5_input.txt","rt")

n,m=map(int,input().split())

N_poly = list(range(1,n+1))
M_poly = list(range(1,m+1))

summ=[sum([x,y]) for x in N_poly for y in M_poly]
value_list=list(range(min(summ),max(summ)+1))
summarize = [summ.count(i) for i in value_list]
out=[value_list[idx] for idx,x in enumerate(summarize) if x == max(summarize)]
print(*out)
#[ for x in summarize if x == max(summarize)]