for _ in range(int(input())):
    n=int(input())
    print(n<<1)
    t=int((len(bin(n))-2)*"1",2)
    print(n*(n^(t)))
