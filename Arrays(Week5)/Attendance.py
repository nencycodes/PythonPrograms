n = int(input())
attendnace = list(map(int, input().split()))
current_streak = 0
max_streak =0
for a in attendnace :
    if a == 0:
        current_streak = current_streak + 1
        max_streak = max(current_streak, max_streak)
    else:
        current_streak = 0
print(max_streak)            