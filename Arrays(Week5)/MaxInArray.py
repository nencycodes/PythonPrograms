n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter the numbers: ").split()))

print("The array is:", arr)

Max = arr[0]

for i in range(len(arr)):
    if Max < arr[i]:
        Max = arr[i]

print("The maximum element in array is:", Max)
#ans = -float("inf")
#if ans< arr[i]
