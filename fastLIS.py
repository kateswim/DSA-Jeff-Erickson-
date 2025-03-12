import math

s= [1,6,2,45,4,90,98,101,8,9,104,230,34,30,400]

def fastLIS(dp):
    s = [-math.inf]+s # make sure every element in s[1:] is greater than s[0]
    n = len(s)-1
    dp=[]
    for i in range(n+1):
        row = [0] * (n+1)  
        dp.append(row) 
    
    for j in range(n,0,-1): # s[0] is infifnity, we do not need incuded
        for i in range(0,j):
            keep=dp[j][j+1]
            skip=dp[i][j+1]
            print(keep,skip)
                
            if s[i]<s[j]:
                dp[i][j]=skip
            else:
                dp[i][j]=max(keep,skip)

    return dp[0][1]

print(fastLIS(dp))   