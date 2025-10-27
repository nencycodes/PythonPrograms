s = "I love programming"
words = s.split(" ")
result = ""

for word in words[::-1]:
    result += word[::-1] + " "

print(result.strip())
