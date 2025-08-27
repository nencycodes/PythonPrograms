n = int(input("enter"))
for i in range(1, n+1):
    print("*", end=" ")
    for j in range(n+1-i):
        if (j == 1 or j == n-i):
            print("*", end="")
        else:
            print("-", end="")
    print()