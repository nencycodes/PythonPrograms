n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter the numbers: ").split()))
Sum =0

print("The array is:", arr)
for i in range(len(arr)):
    Sum= Sum + arr[i]
print("Sum of elements of array is:", Sum)    
