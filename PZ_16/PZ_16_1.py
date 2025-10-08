# Блок заданий 1 (V24)
# Создайте класс "Компьютер" с атрибутами "марка", "процессор" и "оперативная память".
# Напишите метод, который выводит информацию о компьютере в формате
# "Марка: марка, Процессор: процессор, Оперативная память: память".


class Computer:
    def __init__(self, brand, processor, ram):
        self.brand = brand
        self.processor = processor
        self.ram = ram
    
    def get_info(self):
        return f"Марка: {self.brand}, Процессор: {self.processor}, Оперативная память: {self.ram}"


if __name__ == "__main__":
    test_comp1 = Computer("Apple", "M1 Pro", "16 GB DDR5")
    print(test_comp1.get_info())
    
    test_comp2 = Computer("Dell", "Intel Core i7-11800H", "32 GB DDR4")
    print(test_comp2.get_info())
