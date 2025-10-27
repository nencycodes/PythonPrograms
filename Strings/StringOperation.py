A = input().strip()
result = A + A

new_result = ""
for ch in result:
    if not ch.isupper():
        new_result += ch

vowels = "aeiouAEIOU"
for v in vowels:
    new_result = new_result.replace(v, '#')
print(new_result)
