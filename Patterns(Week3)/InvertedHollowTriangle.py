n = int(input("enter:"))
for i in range(1,n+1):
    for j in range(i):
        print("*", end ="")
    for k in range(2*n-2*i):
        print(" ", end="")
    for l in range (i):
        print("*", end ="")     
    print()      
