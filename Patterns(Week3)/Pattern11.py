n = int(input("Enter number:"))
for i in range(0,n):
    for j in range(n-i):
        print("*", end =" ")
    for k in range(2*i):
        print(" ", end =" ")
    for l in range(n-i):
        print("*", end =" ")
    print()   
for i in range(1,n+1):
    for k in range(i):
        print("*", end =" ")
    for l in range( 2*n- 2*i):
        print(" ", end =" ")
    for m in range (i):
        print("*", end =" ")
    print()                            
            