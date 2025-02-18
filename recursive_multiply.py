def recursive_multiply(x, y):
    if x==0:
        return 0
    else:
        x=x//2
        y=y*2
        prod=recursive_multiply(x,y)
        if x%2!=0:
            prod=prod+y
        return prod
    
print(recursive_multiply(1456,889))