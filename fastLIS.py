import math

s= [1,6,2,45,4,90,98,101,8,9,104,230,34,30,550]

def fastLIS():
    s_new = [-math.inf]+s # make sure every element in s[1:] is greater than s[0] - infinity
    n = len(s_new)-1
    dp=[]
    for i in range(n+1):
        row = [0] * (n+1)  
        dp.append(row) 
    
    for j in range(n,0,-1): # s[0] is infifnity, we do not need included
        for i in range(0,j):
            keep = dp[j][j+1] if j < n else 0
            skip = dp[i][j+1] if j < n else 0

            #print(keep,skip)
                
            if s_new[i]<s_new[j]:
                dp[i][j]=max(1 + keep, skip)
            else:
                dp[i][j]=skip

            print(f"i={i}, j={j}, keep={keep}, skip={skip}, s[i]={s_new[i]}, s[j]={s_new[j]}, dp[i][j]={dp[i][j]}")

    return max(dp[0])

print(fastLIS())  