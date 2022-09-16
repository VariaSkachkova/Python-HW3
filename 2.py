# 2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

#     [2, 3, 4, 5, 6] => [12, 15, 16];
#     [2, 3, 5, 6] => [12, 15]
num_list = [2, 3, 5, 6]
prod_list = []
size = len(num_list)
right_i = size - 1
product = 1
'''
Функция поиска произведений элементов в списке, содержащем четное количество элементов

'''
def find_products_in_list_with_even_len(num_list, prod_list, size, right_i, product):
    for left_num in num_list[:size//2:1]: 
            right_num = num_list[right_i]
            product = left_num * right_num
            prod_list.append(product)
            right_i -= 1
    return prod_list
'''
Функция поиска произведений элементов в списке, содержащем нечетное количество элементов

'''
def find_products_in_list_with_odd_len(num_list, prod_list, size, right_i, product):
        for left_num in num_list[:size//2 + 1:1]: 
            right_num = num_list[right_i]
            product = left_num * right_num
            prod_list.append(product)
            right_i -= 1
        return prod_list

if size % 2 == 1:
    print(f'Произведение пар чисел в списке: {find_products_in_list_with_odd_len(num_list, prod_list, size, right_i, product)}')

else:
    print(f'Произведение пар чисел в списке: {find_products_in_list_with_even_len(num_list, prod_list, size, right_i, product)}')
