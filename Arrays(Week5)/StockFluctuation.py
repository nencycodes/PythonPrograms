n = int(input())
Stock = list(map(int, input().split()))
count = 0
for i in range(len(Stock)):
    if Stock[i]>Stock[i-1]:
        count = count + 1
print(count)        