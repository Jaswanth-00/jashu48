            # to store index value vowles in given string
a='ddjuvhOHFEFAHBJEHI'
def index_vowel(a):
    out=[]
    i=0
    for i in range(0,len(a)):#while i<len(a):
        if a[i] in 'aeiouAEIOU':
            out=out+[i]
        i+=1
    return out
c=index_vowel(a)
print(c)
