# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. Подумайте, как это можно решить с помощью рекурсии.

# Пример:

#     45 -> 101101
#     3 -> 11
#     2 -> 10
'''Функции для проверки типа вводимых данных'''
def check_input_int():
    is_correct = False
    while not is_correct:
        try:
            number = int(input('Введите целое число: '))
            is_correct = True
        except ValueError:
            print('Неверный ввод, введите число.')
    return number

number = check_input_int()

'''Функция для преобразования десятичного числа в двоичное'''
def convert_decimal_to_binary(number):
    binary = ''
    while number > 0:
        binary = str(number%2) + binary
        number = number//2
    return binary
print(f'Число {number} в двоичной системе равно {convert_decimal_to_binary(number)}')