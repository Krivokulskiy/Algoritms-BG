n = int(input('Inter n: '))
answer = ''
sum = 0

for a in range(1, n):
    if a == n - 1:
        answer = answer + str(a)
    else:
        answer = answer + str(a) + '+'
    sum = sum + a

print(answer, '=', sum)

proof = n * (n - 1) / 2
print(f"{n} * ({n}-1)) /2 = {proof}")
if sum == proof:
    print('correct')

