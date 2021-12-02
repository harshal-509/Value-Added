# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    n,k=map(int,input().split())
    c=0
    ans=n
    while(n>=k):
        a=n//k
        b=n%k
        ans+=a
        n=a+b
    print(ans)
