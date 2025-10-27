s = "I love programming"
words = s.split(" ")
reversed_sentence = ""

for i in range(len(words) - 1, -1, -1):
    reversed_sentence += words[i] + " "

print(reversed_sentence.strip())
