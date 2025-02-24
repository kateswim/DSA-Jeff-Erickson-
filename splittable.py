from nltk.corpus import words

def isword(w):
    return w in words.words()  # Check if w exists in the English dictionary


def splittable(n):
    if len(n)==0:
        return False
    for i in range(len(n)+1):
        if isword((n[:i])):
            if splittable(n[i:]):
                return True