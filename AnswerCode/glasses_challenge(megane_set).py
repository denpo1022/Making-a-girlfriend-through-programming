N = int(input())
n = [[] for i in range(N)]
for i in range(N):
    q = input().split()
    for j in q:
        n[i].append(int(j))

M = int(input())
m = [[] for i in range(M)]
for i in range(M):
    p = input().split()
    for j in p:
        m[i].append(int(j))

count = 0
for i in range(N-M+1):
    for j in range(N-M+1):
        for x in range(i, i+M):
            for y in range(j, j+M):
                if(m[x-i][y-j] != n[x][y]):
                    break
                else:
                    count += 1
            if(m[x-i][y-j] != n[x][y]):
                break
        if(count == M * M):
            print(i, j)
            exit(0)
        else:
            count = 0
