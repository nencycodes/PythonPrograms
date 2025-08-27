A = int(input("Enter a number: "))
B = int(input("Enter a power you want the above no. to be raised to: "))

result = 1  

for i in range(B):
    result *= A

print("The answer of", A, "raised to the power of", B, "is:", result) 
