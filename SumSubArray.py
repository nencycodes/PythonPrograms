def printSubarray(A, Start, End):
    for i in range(Start, End+1):
        print(A[i], end =" ")
    print()
def PrintAllSubArray(A):
    N = len(A)
    for i in range(N):
        for j in range(i,N):
            printSubarray(A,i,j)
A =[1,2,3]
print(PrintAllSubArray) 