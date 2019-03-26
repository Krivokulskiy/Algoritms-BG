a = int(input('a =: '))
b = int(input('b =: '))
c = int(input('c =: '))

if (a+c<=c) or (a+c<=b) or (b+c<=a):
    print(' This is a triangle')
elif (a!= b) and (a!=c) and  (b!=c):
    print('Triangle is versatile ')
elif a == b == c:
    print('Triangle is equilateral')
else:
    print('Triangle is isosceles')






