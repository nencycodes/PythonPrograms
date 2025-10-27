n = int(input("Enter size of array: "))

arr = list(map(int, input("Enter the numbers: ").split()))
print("The array is:", arr)
Target = int(input("Enter target element:"))
Count =0
for i in range(len(arr)):
    if Target == arr[i]:
        Count = Count+1
print("The no. of time", Target,"appears is", Count)        