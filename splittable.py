from nltk.corpus import words
import time

word_set = set(words.words()) 

def isword(w):
    return w in word_set  # Check if w exists in the English dictionary


def splittable1(n):
    if len(n)==0:
        return True
    for i in range(1, len(n)+1):
        if isword((n[:i])):
            if splittable1(n[i:]):
                return True
    return False
            
n=str('bedbathandbeyond')

start_time = time.time()
result = splittable1(n)
end_time = time.time()
print(f"splittable1 Result: {result}")
print(f"splittable1 Execution Time: {end_time - start_time:.6f} sec")


def splittable2(i):
    if i==len(n):
        return True
    for j in range(i+1, len(n)+1):
        if isword((n[i:j])):
            if splittable2(j):
                return True
    return False

i=0
start_time = time.time()
result2 = splittable2(i)
end_time = time.time()
print(f"splittable2 Result: {result2}")
print(f"splittable2 Execution Time: {end_time - start_time:.6f} sec")
