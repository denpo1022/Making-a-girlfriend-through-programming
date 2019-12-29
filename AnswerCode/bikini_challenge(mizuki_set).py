N = int(input())

five_count = 0
for i in range(1, N+1):
    n = i

    while(n % 5 == 0):
        n /= 5
        five_count += 1

ans = 1
for i in range(1, N+1):
    n = i

    while(n % 5 == 0):
        n /= 5
    while(n % 2 == 0 and five_count > 0):
        n /= 2
        five_count -= 1

    ans *= n
    ans %= 1000000000

print(int(ans))
