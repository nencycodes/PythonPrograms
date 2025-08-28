n = int(input("Enter value :"))
for i in range (0,n):
    for k in range(i):
        print("_", end =" ")
    for k in range(2 *(n - i)- 1):
        print("*", end=" ")    
    print()    