n= input('Inter n: ')
gen_num=1
sum=0
for a in range(0,(int(n))):
    dl = abs((gen_num * 1.5))
    print(f"gen_num is: {gen_num} dl is: {dl} ")
    if gen_num>0:
        sum = sum + gen_num
        gen_num=gen_num-dl

    else:
        sum = sum + gen_num
        gen_num=gen_num+dl


    print (f'gen_num is:', {gen_num}, 'sum is:', {sum})

