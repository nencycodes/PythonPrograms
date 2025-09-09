n = int (input())
for i in range(1, n+1):
    for j in range(1,n+1):
        if(i==1 or i ==5):
            print("*" , end =" ")
        else:
            if((i==2 or i ==3 or i==4) and (j==1 or j==2)):
                print("*", end =" ")
    print()            
                    