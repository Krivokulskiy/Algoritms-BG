opr = ''
a = int(input('Inter a,:'))
b = int(input('Inter b,:'))

while opr not in { '-', '+', '*', '/','0'}:
    print (f"Operand is not selected: {opr} is nor correct")
    opr = input('Select operand: (+, -, /, *), inter 0 for exit ' )

    if opr == 0:
        print('Exit')
        break

    if opr =='+':
        print (a+b)

    if opr =='-':
        print (a-b)

    if opr =='/':
        if b==0:
            print ('Error : divider is zero')
            break
        else:
            print (a/b)

    if opr =='*':
        print (a*b)










