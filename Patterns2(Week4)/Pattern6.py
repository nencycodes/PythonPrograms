n = int(input())
for i in range(1,n+1):
    for j in range(n-i+1):
        print("*", end =" ")
    print()
for i in range(2, n+1):
    for k in range(i):
        print("*", end=" ")
    print()            