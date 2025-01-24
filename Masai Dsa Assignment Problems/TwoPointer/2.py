#2. Non Vowel Substring 

s=input()

i=0
j=0
mxLen = 0
while i<len(s) and j<len(s):
    while i<len(s) and s[i] in 'aeiou':
        i+=1
    j=i
    while j<len(s) and s[j] not in 'aeiou':
        j+=1
    
    if mxLen<j-i:
        mxLen = j-i
    i=j
print(mxLen)
        
        