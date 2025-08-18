N = int(input("Enter a number:"))
print("All the odd numbers from 1 to",N )
for i in range (1, N +1):
    if (i %2!= 0):
        print(i)