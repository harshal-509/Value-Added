for _ in range(int(input())):
    n=int(input())
    l=[]
    for i in range(n):
        a=list(map(int,input().split()))
        l.append(a)
    ans=0
    for i in range(n):
        ans+=l[0][i]
        ans+=l[n-1][i]
    for i in range(1,n-1):
        ans+=l[i][0]
        ans+=l[i][n-1]
    for i in range(1,n-1):
        ans+=l[i][i]
        ans+=l[i][n-i-1]
    if(n%2):
        ans-=l[n//2][n//2]
    print(ans)
