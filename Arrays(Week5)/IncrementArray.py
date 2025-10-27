
n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter the numbers: ").split()))
inc = int(input("Enter increment value: "))
New_Arr = []

for i in range(n):
    New_Arr.append(arr[i] + inc)

print("Original array:", arr)
print("New array:", New_Arr)
