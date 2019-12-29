n = int(input())
m = int(input())
for i in range(m):
    if(int(i / n) & 1):
        print('W', end='')
    else:
        print('R', end='')
