def subset_sum(x,t):
    if t==0:
        return True
    if len(x)==0 and t!=0:
        return False
    else:
        wth=subset_sum(x[1:],t-x[0])
        print(x,t,x[0])
        wout=subset_sum(x[1:],t)
        print(x,t,x[0])
        return wth or wout
    
print(subset_sum([2,4,6,8],10))