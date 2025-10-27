n = int(input())
for i in range(n):
    carNo = int(input())   
    evenSum = 0
    oddSum = 0
    temp = carNo

    while temp > 0:
        lastDigit = temp % 10
        if lastDigit % 2 == 0:
            evenSum += lastDigit
        else:
            oddSum += lastDigit
        temp //= 10

    if (evenSum % 4 == 0) or (oddSum % 3 == 0):
        print("Yes")
    else:
        print("No")
 