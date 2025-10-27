n = int(input())
Gift_Codes = list(map(int,input().split()))
Unique_Codes =[]
for i in range(len(Gift_Codes)):
    if Gift_Codes.count(Gift_Codes[i]) == 1:
        Unique_Codes.append(Gift_Codes[i])
if Unique_Codes:
    print(Unique_Codes) 
else:
    print("-1")           
        