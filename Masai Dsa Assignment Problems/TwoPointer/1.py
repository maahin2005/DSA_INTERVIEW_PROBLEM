#team of heroes 

# target  equal to the sum of two values 

for i in range(int(input())):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))


    i=0
    j=n-1
    ans='No'
    while i<j:
        if arr[i]+arr[j]==k:
            ans='Yes'
            break
        elif arr[i]+arr[j]<k:
            i+=1
        else:
            j-=1
    
    print(ans)