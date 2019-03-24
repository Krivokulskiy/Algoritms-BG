def revers_num (num):
    print (f'Len for {num} is: ', len(num))
    revers =''

    for a in range((len(num)-1),-1,-1):
        revers = revers+num[a]

    return revers

print('Rever num is: ',revers_num(input('Iner a num: ')))


