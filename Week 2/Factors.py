number = int(input("Enter a number:"))
factors = 1
while(factors<=number):
    if(number % factors ==0):
        print(factors)
    factors = factors +1    