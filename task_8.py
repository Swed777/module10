print('Задача 8. Пирамидка')
print('--------------------------')

# Напишите программу,
# которая выводит на экран равнобедренный треугольник (пирамидку),
# заполненный символами хэштега "#". Пусть высота пирамиды вводится пользователем.


# Подсказка: вспомните, как выводился колонтитул вида -----!!!!!!-----

   #
  ###
 #####
#######

h = int(input('Введите высоту рввнобедренного треугольника: '))
print('--------------------------')
print()


width = h + (h - 1)   # вычисляем основание треугольника в зависимости от высоты

for line in range(1, width + 1, 2):
    print(((width - line) // 2) * ' ' + line * '#' + (width - line // 2) * ' ')



print()
print('--------------------------')
