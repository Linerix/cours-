from random import randint
n = 5
m = [[randint(0,100) for i in range(n)]   for j in range(n)]
max_element = max(max(v) for v in m)
print(m)
print(max_element)