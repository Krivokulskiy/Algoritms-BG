def wich_num (num):
    print (f'Len for {num} is: ', len(num))
    Pos= 0
    Neg= 0

    for a in range(len(num)):
        if int(num[a])%2 ==0:
            Pos=Pos+1
        else:
            Neg=Neg+1
    return Pos, Neg

print (wich_num (input('Inter a num: ')))





