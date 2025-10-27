n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter the numbers: ").split()))
Target = int(input("Enter target:"))
for i in range(len(arr)):
    if (Target== arr[i]):
        print("Array found at", i)