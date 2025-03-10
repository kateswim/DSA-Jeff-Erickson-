from nltk.corpus import words
import time

word_set = set(words.words()) 

def isword(w):
    global word_set
    #print(f"word_set {word_set}")
    print(f"word: {w}")
    return w in word_set  # Check if w exists in the English dictionary

def fast_splittable(table):
    table[n+1]=True
    for i in range(n, -1, -1):
        table[i]=False
        for j in range(i,n+1):
            if isword(s[i:j]) and table[j+1]:
                table[i]=True
                print(f"table[i] {table[i]}")
                print(f"table[j] {table[j]}")
                print(f"table {table}")
                #break
    print(f"table {table}")
    return table[0]

s='bedbathandbeyondyoutakingtoolongisunbearable'
n=len(s)
table=[False]*(n+2)
print(fast_splittable(table))
