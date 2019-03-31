count =0
for a in range (32,127):
    print('ASCCI is : ', chr(a), 'code is: ', a, end=',')
    count +=1
    if count ==10:
        print(' END OF DEX')
        count =0

