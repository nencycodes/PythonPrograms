n = int(input())
count = 0
for i in range(n):
    l = list(map(int,input().split()))
    marks = l[0]
    attendance = l[1]
    if( marks>= 75 and attendance>= 80):
        count = count + 1
print(count)   
print(l)     