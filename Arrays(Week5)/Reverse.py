n = int(input())
L = list(map(int,input().split()))
for i in range(len(L)-1, -1, -1):
    print(L[i], end = " ")
    