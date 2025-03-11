import math

s= [1,6,2,45,4,90,98,101,8,9,104,230,34,30,400]

def fastLIS(list):
    n=len(s)
    s[0]= -math.inf
    for i in range(0,n):
        list[i][n+1]=0
    
    for j in range(n,-1,-1):
        for i in range(0,j-1):
            keep=list[j][j+1]
            skip=list[i][j+1]
                
            if s[i]<s[j]:
                list[i][j]=skip
            else:
                list[i][j]=max(keep,skip)

    return list[0][1]

list=[0]*len(s)
print(fastLIS(list))   