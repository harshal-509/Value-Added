for _ in range(int(input())):
    l=list(map(int,input().split()))
    n=len(l)
    l.sort()
    if(len(l)%2==0):
        print(l[len(l)//2])
    else:
        x=10000000
        a=0
        for i in range(n):
            ans=0
            for j in range(n):
                ans+=abs(l[i]-l[j])
            
            if(x>ans):
                x=ans
                a=l[i]
        print(a)
