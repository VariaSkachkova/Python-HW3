# 2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

#     [2, 3, 4, 5, 6] => [12, 15, 16];
#     [2, 3, 5, 6] => [12, 15]
num_list = [2, 3, 5, 6, 9]
prod_list = []
size = len(num_list)
right_i = size - 1
product = 1
if size % 2 == 1:
    for left_num in num_list[:size//2 + 1:1]: 
        right_num = num_list[right_i]
        product = left_num * right_num
        prod_list.append(product)
        right_i -= 1
else:
    for left_num in num_list[:size//2:1]: 
        right_num = num_list[right_i]
        product = left_num * right_num
        prod_list.append(product)
        right_i -= 1

print(prod_list)
