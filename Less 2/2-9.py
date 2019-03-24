def analyze_num (num):
    sumary = 0
    for a in range(0, len(num)):
        sumary=sumary+int(num[a])

    return sumary

check_list=[]

while True:
    new_num= (input('Inter next num or type exit for finish inter num: '))
    if new_num == 'exit':
        break

    check_list.append(new_num)
    print(check_list)

buf = 0
find = 0
for a in range (0, len(check_list)):
    if buf < analyze_num(check_list[a]):
        buf = analyze_num(check_list[a])
        find = check_list[a]

print('Find one: ', find)















