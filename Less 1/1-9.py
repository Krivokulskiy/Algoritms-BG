first = int(input('Enter a first num: '))
second = int(input('Enter a second num: '))
third = int(input('Enter a third num: '))

if first < second < third or third < second < first:
    print('midscore is :', second)
elif first < third < second or second < third < first:
        print('midscore is :', third)
else:
    print('midscore is :', first)
