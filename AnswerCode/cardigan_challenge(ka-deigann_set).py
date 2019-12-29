input_line = int(input())
ans = 1
while(input_line != 1):
    ans *= input_line
    input_line -= 1
print(ans)