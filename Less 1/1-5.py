import string

first_leteral=ord(input('Inter First leteral: '))
second_leteral=ord(input('Inter Second leteral: '))
first_leteral=first_leteral-ord('a')+1
second_leteral=second_leteral-ord('a')+1

print('First leteral is : ', first_leteral, 'Second leteral is: ', second_leteral)
print('Deaposon =', {abs(first_leteral-second_leteral)+1})


list_1=['a','b','c']
a=string.ascii_lowercase
print(a)




