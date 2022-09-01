print('Задача 10. Яма ')
print('--------------------------')

# В одной компьютерной текстовой игре рисуются всяческие элементы ландшафта.
#
# Напишите программу,
# которая получает на вход число N и выводит на экран числа в виде “ямы”:

# Введите число: 5
# 
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345

n = int(input('Введите число N: '))

for i in range(n, 0, -1):
  m = n 
  
  while m > (i - 1):      # левая часть ямы
    print(m, end = '')
    m -= 1
  print(2*(i-1) * '.', end = '')
  
  while m < n:            # правая часть ямы
    print(m + 1, end = '')
    m += 1
    
  print()


print()
print('--------------------------')

'''

Вариант Никиты:

depth = int(input('Введите глубину ямы: '))
for i in range(depth, 0, -1):
  numbers = list(str(num) for num in range(depth, i - 1, -1))
  left, right = ''.join(numbers), ''.join(numbers[::-1])
  dots = '.' * ((depth - len(numbers)) * 2)
  print(left + dots + right)

  '''