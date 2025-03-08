def fast_fibo(n):
    if n==0:
        return (0,1)
    m=n//2
    hprv,hcur=fast_fibo(m)
    prev=hprv*hprv + hcur*hcur
    curr=hcur*(2*hprv+hcur)
    next=prev+curr
    if n%2==0:
        return (prev,curr)
    else:
        return (curr,next)

print(fast_fibo(40))
    