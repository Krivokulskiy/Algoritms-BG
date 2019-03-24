import random

num = random.randint(1,100)
print('IN MEMORY:', num)

while True:
    User_num = int(input('Wath is num? : '))
    if User_num == num:
        print( User_num, 'It is correct')
        break
    elif User_num>num :
        print('Less')
    elif num>User_num:
        print("More")





