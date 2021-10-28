for _ in range(int(input())):
    n=int(input())
    p=int(input())
    ans=0
    arr=[0 for i in range(n+1)]
    for i in range(6,n+1,7):
        if(i<n+1):
            arr[i]=-1
        if(i+1<n+1):
            arr[i+1]=-1
    ans=0
    
    for i in range(p):
        x=int(input())
        for i in range(x,n+1,x):
            if(arr[i]!=-1):
                arr[i]+=1
    for i in range(n+1):
        if(arr[i]!=-1 and arr[i]):
            ans+=1
    print(ans)
