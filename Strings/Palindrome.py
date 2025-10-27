T = int(input())
for _ in range(T):
    s = input().strip()
    if s == s[::-1]:
        print(1)
    else:
        print(0)