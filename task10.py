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


'''
Иду по строчкам

for row in range(n):
  for col in range(2 * n):
    if col == row or col == (2 * n - 1) - row:
      print(n - row, end = '')
    else:
       print('.', end = '')
  print()  
'''

'''
# Иду по строкам

for col in range(2 * n):
  print(n)
  for row in range(n):
     print(col, n - row, end = '')
  '''  

'''
for col_1 in range(n, 0, -1):
  print(col_1, end = '')
for col_2 in range(1, n + 1):
  print(col_2, end = '')
#5432112345
'''

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