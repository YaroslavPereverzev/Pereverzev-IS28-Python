# Блок заданий 2 
# Создайте класс "Человек", который содержит информацию о имени, возрасте и поле.
# Создайте классы "Мужчина" и "Женщина", которые наследуются от класса
# "Человек". Каждый класс должен иметь метод, который выводит информацию о
# поле объекта.

class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"


class Male(Human):
    def __init__(self, name, age):
        super().__init__(name, age, "Male")

    def show_gender(self):
        print("This is a male.")


class Female(Human):
    def __init__(self, name, age):
        super().__init__(name, age, "Female")

    def show_gender(self):
        print("This is a female.")


if __name__ == "__main__":
    person1 = Male("John", 28)
    print(person1.get_info())
    person1.show_gender()

    person2 = Female("Emily", 24)
    print(person2.get_info())
    person2.show_gender()
