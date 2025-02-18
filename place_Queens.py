def place_queens(Q=[], r=0, N=5):
    if r==N:
        print(Q)
    else:
        for i in range(N):
            legal=True
            for j in range(r):
                if Q[j]==i or Q[j]==i+r-j or Q[j]==i-r+j:
                    legal=False
            if legal:
                Q.append(i)
                place_queens(Q, r+1, N=5)
                Q.pop()
                
place_queens(N=8)              
