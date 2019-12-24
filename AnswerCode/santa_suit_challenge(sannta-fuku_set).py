X, Y, Z, N = input().split()
Xcut_point, Ycut_point = [0], [0]
Xcut_point.append(int(X))
Ycut_point.append(int(Y))

for i in range(int(N)):
    d_i, a_i = input().split()
    if(d_i == '1'):
        Ycut_point.append(int(a_i))
    else:
        Xcut_point.append(int(a_i))

if(len(Xcut_point) > 0):
    Xcut_point.sort()
    Xmin = Xcut_point[1] - Xcut_point[0]
    for i in range(len(Xcut_point)):
        if(i == len(Xcut_point) - 1):
            continue
        else:
            if((Xcut_point[i+1] - Xcut_point[i]) < Xmin):
                Xmin = Xcut_point[i+1] - Xcut_point[i]
else:
    Xmin = int(X)

if(len(Ycut_point) > 0):
    Ycut_point.sort()
    Ymin = Ycut_point[1] - Ycut_point[0]
    for i in range(len(Ycut_point)):
        if(i == len(Ycut_point) - 1):
            continue
        else:
            if((Ycut_point[i+1] - Ycut_point[i]) < Ymin):
                Ymin = Ycut_point[i+1] - Ycut_point[i]
else:
    Ymin = int(Y)

print(Xmin * Ymin * int(Z))
