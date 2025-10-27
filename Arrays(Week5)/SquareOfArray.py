n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter the numbers: ").split()))
New_arr=[]
for i in range(len(arr)):
    New_arr.append(arr[i]*arr[i])
print("Square of elements in array is:", New_arr)
