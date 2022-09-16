# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

#     [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
new_list = [2, 3, 5, 9, 3, 7, 4, 1, 2]
index = 1
_sum = 0
'''Функция для поиска суммы чисел, имеющих нечетные индексы в списке'''

def sum_up_odd_idxed_nums(new_list, index, _sum):
    while index <= len(new_list) - 1:
        number = new_list[index]
        _sum += number
        index += 2
    return _sum
print(f'Сумма элементов с нечетными индексами: {sum_up_odd_idxed_nums(new_list, index, _sum)}')


