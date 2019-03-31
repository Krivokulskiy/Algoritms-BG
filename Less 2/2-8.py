### Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
### Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

chek_num=input('Inter num for chek: ')
search_num=str(input('Imsert num for search: '))
count=0



for a in range(0,len(chek_num)):
    if str(chek_num[a]) == search_num:
        count=count+1

print (f"SEARCH:{search_num} in {chek_num}. Find {count}")


