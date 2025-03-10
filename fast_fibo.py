def fast_fibo(n):
    if n == 0:
        return (0, 1)

    m = n // 2
    hprv, hcur = fast_fibo(m)  # Get (F(m-1), F(m))

    prev = hprv * hprv + hcur * hcur  
    curr = hcur * (2 * hprv + hcur)  
    next = prev + curr  

    if n % 2 == 0:
        return (prev, curr)  # Even case: (F(2m-1), F(2m))
    else:
        return (curr, next)  # Odd case: (F(2m), F(2m+1))

print(fast_fibo(40))
print(fast_fibo(50))  
