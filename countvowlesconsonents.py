a='wertyuioASDFGHJXCVBnwertyudfghj'
vowel_count=0
cons_count=0
for var in a:
    if'A'<=var<='Z' or 'a'<=var<='z':
        if var in 'aeiouAEIOU':
            vowel_count+=1
        else:
            cons_count+=1
print(vowel_count,cons_count)                                     