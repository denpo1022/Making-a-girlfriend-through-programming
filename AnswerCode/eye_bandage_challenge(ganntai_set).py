input_line = input()
M1 = input()
x = input().split()
M2 = input()
y = input().split()
ans = []

for i in range(int(M2)):
    if(y[i] not in x):
        ans.append(int(y[i]))

if(len(ans) > 0):
    ans.sort()
    for i in range(len(ans)):
        if(i == len(ans) - 1):
            print(ans[i])
        else:
            print(ans[i], end=' ')
    print()
else:
    print('None')