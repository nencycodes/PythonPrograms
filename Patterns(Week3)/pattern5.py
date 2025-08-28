n = int(input("enter value of n:"))
for i in range(1, n+1):
    for j in range(1, n+1):
        if( j ==1 or j == 5):
            print("*", end ="")
        else:
            print("_", end ="")    
    print()        