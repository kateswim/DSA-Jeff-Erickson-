from nltk.corpus import words
import time

#word_set = set(words.words()) 
word_set = {"bed", "bath", "and", "beyond", "bat", "hand", "bear", "able", "variable", "unbearable"}

def isword(w):
    global word_set
    #print(f"word to check: {w} and word length: {len(w)}")
    if w in word_set:
        print(f"word_set found w in set : {w}")
        return True
    return w in word_set 

def fast_splittable(s,table):
    n=len(s)
    table[n]=True

    for i in range(n, -1, -1):
        table[i]=False
        for j in range(i,n+1):
            if isword(s[i:j]) and table[j+1]:
                table[i]=True
                print(f"table[i] {table[i]}")
                print(f"table[j+1] {table[j+1]}")
                print(f"table \n{table}")
    
    print(f"table {table}")
    return table[0]

#s='bedbathandbeyondyoutakingtoolongisunbearable'
s='bedbathandbeyondvariable'
n = len(s)
table=[False]*(n+2)

print(fast_splittable(s,table))
