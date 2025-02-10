st=[]
s="abc"
for i in range(len(s)):
    if s[i].isalpha():
        st.append(s[i])
    else:
        if st:
            st.pop()
ans=''.join(st)
print(ans)
