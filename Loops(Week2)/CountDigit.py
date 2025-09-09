num = int(input("enter a digit"))
num1 = int(input(" enter a number for digit count"))
count = 0
while num >0:
    last = num%10
    if last==num1:
        count+=1
    num//=10
print(count)