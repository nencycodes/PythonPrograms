n = int(input())
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(j, end =" ")
    for k in range(2, 2*i-1):
        print("*", end =" ")
    print()        