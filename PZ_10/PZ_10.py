# В магазинах имеются следующие товары. Магнит – молоко, соль, сахар.
# Пятерочка – мясо, молоко, сыр. Определить:
# 1. какие товары из Магнита, отсутствуют в Пятерочке.
# 2. какие товары из Пятерочки, отсутствуют в Магните.
# 3. полный перечень всех товаров.
# 4. равны ли перечни товаров.

magnit = {'молоко', 'соль', 'сахар'} 
pyaterochka = {'мясо', 'молоко', 'сыр'}

# 1
missing_in_pyaterochka = magnit.difference(pyaterochka)  # difference возвращает элементы, которые есть в magnit, но отсутствуют в pyaterochka
print("Товары из Магнита, отсутствующие в Пятерочке:", missing_in_pyaterochka)

# 2
missing_in_magnit = pyaterochka.difference(magnit)  # difference возвращает элементы, которые есть в pyaterochka, но отсутствуют в magnit
print("Товары из Пятерочки, отсутствующие в Магните:", missing_in_magnit)

# 3
all_products = magnit.union(pyaterochka)  # union объединяет два множества, возвращая все уникальные элементы
print("Полный перечень всех товаров:", all_products)

# 4
are_equal = magnit == pyaterochka
print("Перечни товаров равны:", are_equal)
