N = int(input("Enter number:"))
for i in range (1,N+1):
    for j in range(i):
        print("*", end =" ")
    print()    
for i in range(1,N):
    for j in range(N-i):
        print("*", end = " ")
    print()        