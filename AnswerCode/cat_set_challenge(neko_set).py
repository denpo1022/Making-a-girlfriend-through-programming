input_line = input()
cat_count, c_count, a_count, t_count = 0, 0, 0, 0

c_count = input_line.count('c')
a_count = input_line.count('a')
t_count = input_line.count('t')

min_count = min(c_count, a_count, t_count)
max_count = max(c_count, a_count, t_count)

if(min_count != 0):
    cat_count = min_count
    c_count, a_count, t_count = c_count - \
        cat_count, a_count-cat_count, t_count-cat_count
    min_count = 0
    max_count -= cat_count

print(cat_count)
print(max_count - c_count)
print(max_count - a_count)
print(max_count - t_count)
