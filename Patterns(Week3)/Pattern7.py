n = int(input("Enter value: "))

for i in range(1, n+1):
    # print leading underscores for alignment
    for j in range(n-i):
        print("_", end=" ")
    # print stars with spaces in between (for symmetry)
    for k in range(i):
        print("*", end="  ")   # <-- two spaces after star
    print()
