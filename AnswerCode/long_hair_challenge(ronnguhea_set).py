yes_count, no_count = 0, 0
for i in range(5):
    input_line = input()
    if(input_line == 'yes'):
        yes_count += 1
    else:
        no_count += 1
if(yes_count > no_count):
    print('yes')
else:
    print('no')