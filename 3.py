# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

#     [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
#         [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91
new_list = [4.07, 5.1, 8.2444, 6.98]
idx = 0
min_fraction = new_list[0] - new_list[0]*10//10
max_fraction = new_list[0] - new_list[0]*10//10
while idx < len(new_list):
    fraction = new_list[idx] - new_list[idx]*10//10
    if fraction > max_fraction:
        max_fraction = fraction
    else:
        if fraction < min_fraction:
            min_fraction = fraction
    idx += 1
print(max_fraction, min_fraction)
dif = round(max_fraction - min_fraction, 5)
print(dif)

