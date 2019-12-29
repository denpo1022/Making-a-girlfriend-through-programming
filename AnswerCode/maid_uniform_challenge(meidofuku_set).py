N = int(input())
for i in range(N):
    m = int(input())
    if(m == 0):
        print('01:00')
    else:
        m /= 3
        minute = int(60 - m)
        if(minute >= -90 and minute <= -60):
            if(minute == -60):
                print('23:00')
            else:
                print('22:' + '{0:0=2d}'.format(120 + minute))
        elif(minute > -60 and minute <= 0):
            if(minute == 0):
                print('00:00')
            else:
                print('23:' + '{0:0=2d}'.format(60 - abs(minute)))
        else:
            print('00:' + '{0:0=2d}'.format(minute))
