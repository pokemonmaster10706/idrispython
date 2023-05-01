import decimal_checking as d

a = int(input('enter side a:'))
b = int(input('enter side b:'))

area = (a*b)/2
d.decimal(area)

print('area of the triangle is:',d.decimal(area))
