n = int(input("enter"))
for i in range(0, n):
    for k in range(i):
        print("-", end = "")
    for j in range(n-i):
        print("*", end ="")    
    print()        