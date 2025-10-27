n = int(input())
arr = list(map(int,input().split()))
count = 0
count1 = 0
for i in range (len(arr)):
    if arr[i]<= 35:
        count = count +1
    else:
        count1 = count1+ 1  
print(count)
print(count1)