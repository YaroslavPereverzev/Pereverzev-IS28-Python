# Приложение ВЫДАЧА КРЕДИТОВ для некоторой организации. БД должна
# содержать таблицу Клиент со следующей структурой записи: ФИО клиента, ФИО
# сотрудника банка, срок кредита, процент кредита, сумма кредита.

import sqlite3


def connect_db(db_name="credit_db.sqlite"):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    return connection, cursor


def create_table(cursor):
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Клиент (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            фио_клиента TEXT NOT NULL,
            фио_сотрудника TEXT NOT NULL,
            срок_кредита INTEGER NOT NULL,
            процент_кредита REAL NOT NULL,
            сумма_кредита REAL NOT NULL
        )
    """)
    return True


def insert_client(connection, cursor, client_data):
    cursor.execute("""
        INSERT INTO Клиент (фио_клиента, фио_сотрудника, срок_кредита, процент_кредита, сумма_кредита)
        VALUES (?, ?, ?, ?, ?)
    """, client_data)
    connection.commit()
    return True


def find_clients(cursor):
    print("\nВарианты поиска клиентов:")
    print("1. По ФИО клиента")
    print("2. По сумме кредита (больше указанной)")
    print("3. По сроку кредита (меньше указанного)")

    choice = input("Выберите вариант поиска (1-3): ")

    try:
        if choice == "1":
            name = input("Введите ФИО клиента для поиска: ")
            cursor.execute("SELECT * FROM Клиент WHERE фио_клиента LIKE ?", (f"%{name}%",))
        elif choice == "2":
            amount = float(input("Введите минимальную сумму кредита: "))
            cursor.execute("SELECT * FROM Клиент WHERE сумма_кредита > ?", (amount,))
        elif choice == "3":
            term = int(input("Введите максимальный срок кредита (в месяцах): "))
            cursor.execute("SELECT * FROM Клиент WHERE срок_кредита < ?", (term,))
        else:
            return []

        return cursor.fetchall()

    except ValueError:
        return []
    except sqlite3.Error:
        return []


def delete_client(connection, cursor):
    print("\nВарианты удаления клиентов:")
    print("1. По ФИО клиента")
    print("2. По ФИО сотрудника")
    print("3. По идентификатору (id)")

    choice = input("Выберите вариант удаления (1-3): ")

    try:
        if choice == "1":
            name = input("Введите ФИО клиента для удаления: ")
            cursor.execute("DELETE FROM Клиент WHERE фио_клиента LIKE ?", (f"%{name}%",))
        elif choice == "2":
            employee = input("Введите ФИО сотрудника для удаления связанных клиентов: ")
            cursor.execute("DELETE FROM Клиент WHERE фио_сотрудника LIKE ?", (f"%{employee}%",))
        elif choice == "3":
            client_id = int(input("Введите ID клиента для удаления: "))
            cursor.execute("DELETE FROM Клиент WHERE id = ?", (client_id,))
        else:
            return

        connection.commit()
        return cursor.rowcount

    except ValueError:
        return
    except sqlite3.Error:
        return


def update_client(connection, cursor):
    print("\nВарианты поиска клиента для редактирования:")
    print("1. По ФИО клиента")
    print("2. По идентификатору (id)")
    print("3. По сумме кредита (точное совпадение)")

    choice = input("Выберите вариант поиска (1-3): ")

    try:
        if choice == "1":
            name = input("Введите ФИО клиента для редактирования: ")
            cursor.execute("SELECT * FROM Клиент WHERE фио_клиента LIKE ?", (f"%{name}%",))
        elif choice == "2":
            client_id = int(input("Введите ID клиента для редактирования: "))
            cursor.execute("SELECT * FROM Клиент WHERE id = ?", (client_id,))
        elif choice == "3":
            amount = float(input("Введите сумму кредита для поиска клиентов: "))
            cursor.execute("SELECT * FROM Клиент WHERE сумма_кредита = ?", (amount,))
        else:
            return

        clients = cursor.fetchall()
        if not clients:
            return

        for client in clients:
            print(f"ID: {client[0]}, Клиент: {client[1]}, Сотрудник: {client[2]}, "
                  f"Срок: {client[3]} мес., Процент: {client[4]}%, Сумма: {client[5]} руб.")

        client_id = int(input("\nВведите ID клиента для редактирования: "))

        print("\nКакие данные изменить?")
        print("1. ФИО клиента")
        print("2. ФИО сотрудника")
        print("3. Срок кредита")
        print("4. Процент кредита")
        print("5. Сумму кредита")
        field_choice = input("Выберите поле для изменения (1-5): ")

        fields = {
            "1": "фио_клиента",
            "2": "фио_сотрудника",
            "3": "срок_кредита",
            "4": "процент_кредита",
            "5": "сумма_кредита"
        }

        if field_choice not in fields:
            return

        new_value = input(f"Введите новое значение для поля '{fields[field_choice]}': ")

        if field_choice in ("3", "4", "5"):
            try:
                new_value = float(new_value)
                if field_choice == "3":
                    new_value = int(new_value)
            except ValueError:
                return

        cursor.execute(
            f"UPDATE Клиент SET {fields[field_choice]} = ? WHERE id = ?",
            (new_value, client_id)
        )
        connection.commit()
        return True

    except ValueError:
        return
    except sqlite3.Error:
        return


def display_all_clients(cursor):
    cursor.execute("SELECT * FROM Клиент")
    clients = cursor.fetchall()

    if not clients:
        return

    print("\nСписок всех клиентов:")
    print("-" * 80)
    print("ID | Клиент | Сотрудник | Срок (мес.) | Процент (%) | Сумма (руб.)")
    print("-" * 80)
    for client in clients:
        print(f"{client[0]} | {client[1]} | {client[2]} | {client[3]} | {client[4]} | {client[5]}")
    print("-" * 80)


def input_client_data():
    try:
        client_name = input("ФИО клиента: ")
        if not client_name:
            return None

        employee_name = input("ФИО сотрудника банка: ")
        if not employee_name:
            return None

        term = int(input("Срок кредита (в месяцах): "))
        if term <= 0:
            return None

        percent = float(input("Процент кредита: "))
        if percent <= 0:
            return None

        amount = float(input("Сумма кредита (руб.): "))
        if amount <= 0:
            return None

        return (client_name, employee_name, term, percent, amount)

    except ValueError:
        return None


def main():
    connection, cursor = connect_db()
    create_table(cursor)

    try:
        cursor.execute("SELECT COUNT(*) FROM Клиент")
        if cursor.fetchone()[0] == 0:
            test_data = [
                ("Иванов Иван Иванович", "Петрова Анна Сергеевна", 12, 10.5, 500000),
                ("Смирнова Елена Владимировна", "Козлов Дмитрий Анатольевич", 24, 12.0, 750000),
                ("Петров Петр Петрович", "Сидорова Ольга Ивановна", 36, 15.0, 1000000),
                ("Кузнецова Мария Андреевна", "Петрова Анна Сергеевна", 12, 9.5, 300000),
                ("Соколов Алексей Дмитриевич", "Козлов Дмитрий Анатольевич", 60, 18.0, 1500000),
                ("Михайлова Татьяна Николаевна", "Сидорова Ольга Ивановна", 24, 11.5, 600000),
                ("Новиков Сергей Васильевич", "Петрова Анна Сергеевна", 36, 13.0, 800000),
                ("Федорова Ольга Петровна", "Козлов Дмитрий Анатольевич", 12, 10.0, 400000),
                ("Алексеев Андрей Викторович", "Сидорова Ольга Ивановна", 48, 16.5, 1200000),
                ("Павлова Екатерина Сергеевна", "Петрова Анна Сергеевна", 24, 12.5, 900000)
            ]
            for data in test_data:
                insert_client(connection, cursor, data)
    except sqlite3.Error:
        pass

    while True:
        print("\nМеню управления базой данных 'Выдача кредитов':")
        print("1. Добавить нового клиента")
        print("2. Поиск клиентов")
        print("3. Удалить клиента")
        print("4. Редактировать данные клиента")
        print("5. Показать всех клиентов")
        print("6. Выход")

        choice = input("Выберите действие (1-6): ")

        if choice == "1":
            client_data = input_client_data()
            if client_data:
                insert_client(connection, cursor, client_data)
        elif choice == "2":
            clients = find_clients(cursor)
            if clients:
                for client in clients:
                    print(f"ID: {client[0]}, Клиент: {client[1]}, Сотрудник: {client[2]}, "
                          f"Срок: {client[3]} мес., Процент: {client[4]}%, Сумма: {client[5]} руб.")
        elif choice == "3":
            delete_client(connection, cursor)
        elif choice == "4":
            update_client(connection, cursor)
        elif choice == "5":
            display_all_clients(cursor)
        elif choice == "6":
            break

    connection.close()


if __name__ == "__main__":
    main()
