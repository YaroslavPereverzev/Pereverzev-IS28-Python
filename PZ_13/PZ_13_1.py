# 1. В матрице найти отрицательные элементы, сформировать из них новый массив. Вывести размер полученного массива
import random


def matrix_negative(matrix):
    return [element for row in matrix for element in row if element < 0]

def make_matrix(from_x, to_x, len_list, len_matrix):
    return [[random.randint(from_x, to_x) for _ in range(len_list)] for _ in range(len_matrix)]

matrix = make_matrix(-10, 10, 3, 3)
for i in matrix:
    print(i)

negative_elements = matrix_negative(matrix)
print(negative_elements)
print(len(negative_elements)) 
