n = int(input("Enter number:"))
original = n
reverse_number = 0

while n != 0:
    next_digit = n % 10
    reverse_number = (reverse_number * 10) + next_digit
    n = n // 10   

print("Reverse of the number is:", reverse_number)

if original == reverse_number:
    print(original, "is a Palindrome.")
else:
    print(original, "is NOT a Palindrome.")
