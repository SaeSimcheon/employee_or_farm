n,m,y,x,k=map(int,input().split())
base=[list(map(int,input().split())) for _ in range(n)]
order=list(map(int,input().split()))

dic={'up':0,'down':0,'east':0,'west':0,'north':0,'south':0}
order_dic={1:(0,1),2:(0,-1),3:(-1,0),4:(1,0)} 

for kk in order:
    y_loc,x_loc=order_dic[kk]
    if 0<=x+x_loc<m and 0<=y+y_loc<n:
        x=x+x_loc # 일단 x,y좌표 갱신은 끝남
        y=y+y_loc #
        if kk==1: # 동
            new_dic={}
            new_dic['up']=dic['west']
            new_dic['down']=dic['east']
            new_dic['east']=dic['up']
            new_dic['west']=dic['down']
            new_dic['north']=dic['north']
            new_dic['south']=dic['south']
            dic=new_dic
            if base[y][x]==0:
                base[y][x]=dic['down']
            else:
                dic['down']=base[y][x]
                base[y][x]=0
#            print(dic)
            print(dic['up'])
        elif kk==2:
            new_dic={}
            new_dic['up']=dic['east']
            new_dic['down']=dic['west']
            new_dic['east']=dic['down']
            new_dic['west']=dic['up']
            new_dic['north']=dic['north']
            new_dic['south']=dic['south']
            dic=new_dic
            if base[y][x]==0:
                base[y][x]=dic['down']
            else:
                dic['down']=base[y][x]
                base[y][x]=0
#            print(dic)
            print(dic['up'])
        elif kk==3:
            new_dic={}
            new_dic['up']=dic['south']
            new_dic['down']=dic['north']
            new_dic['east']=dic['east']
            new_dic['west']=dic['west']
            new_dic['north']=dic['up']
            new_dic['south']=dic['down']
            dic=new_dic
            if base[y][x]==0:
                base[y][x]=dic['down']
            else:
                dic['down']=base[y][x]
                base[y][x]=0
#            print(dic)
            print(dic['up'])
        else:
            new_dic={}
            new_dic['up']=dic['north']
            new_dic['down']=dic['south']
            new_dic['east']=dic['east']
            new_dic['west']=dic['west']
            new_dic['north']=dic['down']
            new_dic['south']=dic['up']
            dic=new_dic
            if base[y][x]==0:
                base[y][x]=dic['down']
            else:
                dic['down']=base[y][x]
                base[y][x]=0
#            print(dic)
            print(dic['up'])
