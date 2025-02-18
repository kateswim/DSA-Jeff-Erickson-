# def tower_of_Hanoi(n,src,dst,tmp):
#     if n==0:
#         return 
#     else:
#         tower_of_Hanoi(n-1,src,tmp,dst)
#         print("Move disk",n,"from",src,"to",dst)
#         tower_of_Hanoi(n-1,tmp,dst,src)

# n = 3
# tower_of_Hanoi(n, 'A', 'C', 'B')

def hanoi(n, src, dst, tmp):
    if n == 0:
        "this is moved!"
    elif n > 0:
        hanoi(n-1, src, tmp, dst) # n=3 first call hanoi(2, "S", "T", "D")
                                # n= 2 first call hanoi(1, "S", "D", "T")
                                # n= 1 first call hanoi(0, "S", "T", "D")
        print(f"Move disk:{n} from source:{src} to destination:{dst}") # n=3 print "Move disk:3 from source:S to destination:D"
                                                                    

        hanoi(n-1, tmp, dst, src) # n=3 second call hanoi(2, "T", "D", "S")
                                # n= 2 second call hanoi(1, "T", "S", "D")
                                # n= 1 second call hanoi(0, "T", "D", "S")
    

hanoi(1, "S", "D", "T")