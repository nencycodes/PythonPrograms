n = int(input("enter number:"))
for i in range(1,n+1):
    for k in range(i):
        print("*", end =" ")
    for l in range( 2*n- 2*i):
        print(" ", end =" ")
    for m in range (i):
        print("*", end =" ")
    print()                         