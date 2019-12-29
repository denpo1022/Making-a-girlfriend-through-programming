input_line = int(input())
string = ''
for i in range(input_line):
    string += input() + '_'
print(string[:len(string)-1])