n=[1,6,2,45,4,90,98,101,8,9,104,230,34,30,400]
def LISfirst(i):
    best=0
    for j in range(i+1,len(n)):
        if n[j]>n[i]:
            best=max(best,LISfirst(j))
            print(n[best])

    return best+1

print(LISfirst(3))
