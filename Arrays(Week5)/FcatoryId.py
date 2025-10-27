n = int(input())
IDs = list(map(int, input().split()))
ID2 = []
for i in range(len(IDs)):
    if IDs[i] % 5 ==0:
        ID2.append(IDs[i])
if len(ID2) == 0:
    print("-1")
else:
    ID2.sort(reverse=True)    
    print(ID2)