n = int(input())
arr = list(map(int, input().split()))
count = 0
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        print(arr[i], end=" ")
        count += 1
if count == 0:
    print(-1)
