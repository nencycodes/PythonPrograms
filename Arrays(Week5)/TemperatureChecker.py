n = int(input())
Temperature = list(map(int,input().split()))
count = 0
for i in range(len(Temperature)):
    if(Temperature> 40):
        count = count+1
print(count)        