n = int(input("Enter number:"))
for i in range(0,n):
    for j in range(n-i):
        print("*", end =" ")
    for k in range(2*i):
        print(" ", end =" ")
    for l in range(n-i):
        print("*", end =" ")
    print()    
            