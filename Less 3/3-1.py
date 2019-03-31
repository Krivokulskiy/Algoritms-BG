"""1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9."""

main_array = [ _ for _ in range(2,99)]
advance_array = [_ for _ in range(2,9)]
print('Crated  main_array:')
print(main_array)

print('Crated  advance_array:')
print(advance_array)

count=0
for i in advance_array:
    count=0
    print(f"Check for: {i}")
    for j in main_array:
        if j % i == 0:
            count = count+1
            print(f"Status: {j} / {i} multiple found")
    print(f"Total multiple for {i} found: {count}")













