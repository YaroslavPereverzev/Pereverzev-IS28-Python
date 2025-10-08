# 2. Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее элементов.
import random

def make_matrix(from_x, to_x, len_list, len_matrix):
    return [[random.randint(from_x, to_x) for _ in range(len_list)] for _ in range(len_matrix)]

def average_matrix_odd(matrix):
    return [round(sum(row) / len(row), 2) for i, row in enumerate(matrix, 1) if i % 2 != 0]

matrix = make_matrix(-10, 10, 3, 3)
for i in matrix:
    print(i)

average = average_matrix_odd(matrix)
print(average)
