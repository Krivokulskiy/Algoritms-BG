import random

star_point = int(input('star point: '))
end_point = int(input('end point: '))
print (random.randint(star_point, end_point))

star_point = float(input('star point: '))
end_point = float(input('end point: '))
print (random.randint(star_point, end_point))

star_point = ord(input('star point: '))
end_point = ord(input('end point: '))
result = random.randint(star_point, end_point)
print(chr(result))

