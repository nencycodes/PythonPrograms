A = input().strip()
B = input().strip()
if B in A:
    print(A.index(B))
else:
    print(-1)