i  = [1, 8, 7, 1, 3, 2, 3, 'hello', 'abc', 'hello']
x = []
y = []
for line in i:
    if line not in x:
        x.append(line)
    elif line in x:
        y.append(line)
print(y)
print(x)

