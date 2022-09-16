# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

#     [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
#         [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

new_list = [4.07, 5.1, 8.2444, 6.98]

'''Функция, создающая отдельный список только с дробной частью чисел.'''
def leave_only_fractions(new_list):
    fract_list = []
    for i in new_list:
        i = i - i * 10 //10
        fract_list.append(i)
    return fract_list
    
# Я сначала сделала поиск максимального и минимального значения в рамках одной функции, 
# но у меня не получилось придумать, как вернуть сразу два значения в следующую функцию.
'''Функция для поиска максимального значения.'''
def find_max(_list):
    _max = fract_list[0]
    for i in fract_list[1:]:
        if i > _max:
            _max = i      
    return _max

'''Функция для поиска минимального значения.'''
def find_min(_list):
    _min = fract_list[0]
    for i in fract_list[1:]:
        if i < _min:
            _min = i      
    return _min

'''Функция для поиска разницы между значениями.'''  
def find_dif_between_min_and_max (_max, _min):
    dif = round(_max - _min, 5)
    return dif

fract_list = leave_only_fractions(new_list)
print(f'Разность между максимальным и минимальным значением дробной части элементов: {find_dif_between_min_and_max(find_max(fract_list), find_min(fract_list))}')

