def prime(n):
    for i in range(2,n):
        if(n%i==0):
            #print(n,i)
            return False
    return True
for i in range(int(input())):
    n=int(input())
    ans=0
    for i in range(2,n):
        if(prime(i) and prime(2*i+1)):
            ans+=i
    print(ans)
