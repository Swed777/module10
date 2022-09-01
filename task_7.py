print('Задача 7. Наибольшая сумма цифр')
print('--------------------------')
# Вводится N чисел. 
# Среди натуральных чисел, которые были введены, 
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

max_summ = 0
max_num  = 0
numbers_list = input("Введите список чисел, разделенных пробелом: ").split()
num_list = list(map(int, numbers_list)) #приведение к типу int

for i in num_list:
  sum = 0
  tmp_i = i
  while tmp_i != 0:
        sum += tmp_i % 10
        tmp_i //= 10
  if sum > max_summ:
    max_summ = sum 
    max_num = i
print('Наибольшее число по сумме цифр: ', max_num, 'а сумма этого числа = ', max_summ)  

print('--------------------------')
