x = int(input())
y = int(input())
p = int(input())
years = 0
while x < y:
    i = x * p // 100
    x += i
    years += 1
print('вы накопите', x, 'через', years, 'лет')