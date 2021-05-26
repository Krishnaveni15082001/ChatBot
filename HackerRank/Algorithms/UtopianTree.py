t=int(input())
for i in range(t):
    st=int(input())
    res=1
    for j in range(st):
        if (j%2)==0:
            res*=2
        else:
            res+=1
    print(res)

