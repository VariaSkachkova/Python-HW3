# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

#     для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
n = 8

def fibonacci_pos(n):
    if (n == 1 or n == 2):
         return 1
    else:
        return fibonacci_pos(n - 1) + fibonacci_pos(n - 2)

def fibonacci_neg(n):
    
    if (n == -1):
         return 1
    elif (n == -2):
        return -1
    else:
        return fibonacci_neg(n + 2) - fibonacci_neg(n + 1)
# for i in range (-1, n-1, -1):
#     print(fibonacci_neg(i), end = ' ')
n = n * -1
sequence = []
for i in range (-1, n-1, -1):
    sequence.append(fibonacci_neg(i))
sequence.reverse()
# print(sequence)
sequence.append(0)
n = n * -1
for i in range (1, n+1):
    sequence.append(fibonacci_pos(i))
print(sequence)


