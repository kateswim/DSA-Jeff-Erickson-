import time
list=[None]*100

def mem_fibo(n):
    global list
    if n==0:
        return 0
    elif n==1:
        return 1
    elif list[n] == None:
        list[n] = mem_fibo(n-1) + mem_fibo(n-2)
        #return list[n]
    return list[n] 

def mem_fibo_slow(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    return mem_fibo_slow(n-1) + mem_fibo_slow(n-2)
    

time1 = time.time()
print(mem_fibo(40))
time2 = time.time()
print("Time taken by memoized version is ", time2-time1)

time1 = time.time()
print(mem_fibo_slow(40))
time2 = time.time()
print("Time taken by non-memoized version is ", time2-time1)