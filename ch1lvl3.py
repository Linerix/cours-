numb = int(input('введите число:'))
l = 0
while numb > 0:
    i = numb % 10
    l += i
    numb //= 10
print(l)