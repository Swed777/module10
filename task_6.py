print('Задача 6. Сумма факториалов')
print('--------------------------')
# Напишите программу,
# которая запрашивает у пользователя число N
# и находит сумму факториалов 1! + 2! + 3! +... + N! 

fact = 1
summ_fact = 0

number = int(input('Введите число для вычисления суммы факториалов: '))

for i_number in range(1, number + 1):
    for f_act in range(1, i_number + 1):
        fact *= f_act
    summ_fact += fact
    fact = 1

print('Сумма факториалов числа ', number, ': =', summ_fact)


print('--------------------------')