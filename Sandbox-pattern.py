n=int(input())
for i in range(n-1,0,-1):
    for s in range(n-i-1):
        print(" ",end=" ")
    for str in range(2*i+1):
        print("*",end=" ")
    print()
for i in range(1,n+1):
    for s in range(n-i):
        print(" ",end=" ")
    for str in range(2*i-1):
        print("*",end=" ")
    print()


    



    
