T = int(input())
for _ in range(T):
    s = input().strip()
    vowels = "aeiouAEIOU"
    v_count = 0
    c_count = 0
    for char in s:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            if char in vowels:
                v_count += 1
            else:
                c_count += 1
    print(v_count, c_count)