# 2. Из предложенного текстового файла (text18-24.txt) вывести на экран его содержимое, количество символов, 
# принадлежащих к группе букв. Сформировать новый файл, в который поместить текст в стихотворной форме 
# предварительно заменив символы нижнего регистра на верхний.

with open('text18-24.txt', 'r', encoding='utf-8') as f:
    content = f.read()

letter_count = 0
for char in content:
    if char.isalpha():
        letter_count += 1

formatted_content = content.replace('. ', '.\n')

with open('PZ_11_2_results/upper_case_text.txt', 'w', encoding='utf-8') as f:
    for char in formatted_content:
        f.write(char.upper())

print(formatted_content)
print(f'Количество букв: {letter_count}') 