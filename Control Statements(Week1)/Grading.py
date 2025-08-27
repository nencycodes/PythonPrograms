percentage =int(input("Enter the percentage from 0-100:"))
if(percentage<= 100):
    if(percentage>= 85 and percentage<=100):
        print("Grade: A+")
    elif(percentage>= 65 and percentage<= 85):
        print("Grade : A")
    elif(percentage>= 45 and percentage<= 65):
        print("Grade : B")
    elif(percentage>=25 and percentage<= 45):
        print("Grade: C")
    else:
        print("Grade: D")
else:
    print("Invalid percentage")        
                
            
           