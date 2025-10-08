# 1. Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной последовательности из целых положительных и отрицательных чисел. 
# Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Содержимое первого файла:
# Элементы кратные 3:
# Произведение элементов:
# Минимальный элемент:
# Содержимое второго файла:
# Элементы кратные 5:
# Количество элементов:
# Среднее арифметическое элементов:

import random

with open('PZ_11_1_results/first_file.txt', 'w', encoding='utf-8') as f:
    numbers = []
    for i in range(10):
        numbers.append(random.randint(-100, 100))
    f.write(' '.join(map(str, numbers)))

multiples_of_3 = []
product = 1
for num in numbers:
    if num % 3 == 0:
        multiples_of_3.append(num)
        product *= num
min_element = min(numbers)

with open('PZ_11_1_results/result_first_file.txt', 'w', encoding='utf-8') as f:
    f.write(f'Элементы кратные 3: {multiples_of_3}\n')
    f.write(f'Произведение элементов: {product}\n')
    f.write(f'Минимальный элемент: {min_element}\n')

with open('PZ_11_1_results/second_file.txt', 'w', encoding='utf-8') as f:
    second_numbers = []
    for i in range(10):
        second_numbers.append(random.randint(-100, 100))
    f.write(' '.join(map(str, second_numbers)))

multiples_of_5 = []
for num in second_numbers:
    if num % 5 == 0:
        multiples_of_5.append(num)
count_elements = len(second_numbers)
average = sum(second_numbers) / count_elements if count_elements > 0 else 0

with open('PZ_11_1_results/result_second_file.txt', 'w', encoding='utf-8') as f:
    f.write(f'Элементы кратные 5: {multiples_of_5}\n')
    f.write(f'Количество элементов: {count_elements}\n')
    f.write(f'Среднее арифметическое элементов: {average}\n') 