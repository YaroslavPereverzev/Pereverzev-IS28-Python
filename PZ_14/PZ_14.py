# В исходном текстовом файле (Dostoevsky.txt) найти все годы деятельности писателя 
# (например, 1821 года, 1837 год, 1843 году и так далее  по всему тексту). 
# Посчитать количество полученных элементов.

import re

with open('Dostoevsky.txt', 'r', encoding='utf-8') as file:
    text = file.read()

pattern = r'\b18[2-8][0-9]\s*(?:год[ауе]?|гг?\.|годах?)?\b(?:[-–]\s*18[2-8][0-9]\s*(?:год[ауе]?|гг?\.|годах?)?\s*(?:гг?\.)?)?'

matches = re.findall(pattern, text)

print(f"Всего найдено {len(matches)} упоминаний годов:")
for year in matches:
    print(f"- {year}")

print(f"\nОбщее количество упоминаний: {len(matches)}")
