x1= int(input('Inter x1 point1: '))
y1= int(input('Inter y1 point1: '))

x2= int(input('Inter x2 point1: '))
y2= int(input('Inter y2 point1: '))

if x1==x2:
    print(f'x = {x1:.2f}')
else:
    k = (y1-y2)/(x1-x2)
    b = y2-k*x2
    print(f'y = {k:.2f} *x + {b:3f}')





