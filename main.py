def main_menu():
    while True:
        print("Главное меню:")
        print("1. Кол-во разрядов числа")
        print("2. Задание 2")
        print("3. Строка матрицы с положительными элементами")
        print("4. try-except-finally")
        print("5. Выйти")

        choice = input("Выберите пункт меню: ")

        if choice == '1':
            while True:
                usernum = input("Введите число: ")
                if usernum.isdigit():
                    usernum = int(usernum)
                    break
                else:
                    print("Неккоректный ввод. ")
            countnum = len(str(usernum))
            print("Колличество разрядов числа =", countnum)
            pass

        elif choice == '2':
            def process_input():
                print("Выберите тип входных данных:")
                print("1. Число")
                print("2. Строка")
                print("3. Словарь")
                print("4. Список")
                choice = input("Введите номер: ")

                if choice == '1':
                    while True:
                        num = input("Введите число: ")
                        if num.isdigit():
                            num = int(num)
                            break
                        else:
                            print("Неккоректный ввод. ")

                    def is_prime(num):
                        if num < 2:
                            return False
                        for i in range(2, int(num ** 0.5) + 1):
                            if num % i == 0:
                                return False
                        return True

                    if is_prime(num):
                        print("Число", num, "является простым.")
                    else:
                        print("Число", num, "не является простым.")

                elif choice == '2':
                    string = input("Введите строку: ")
                    numbers_sum = sum(int(char) for char in string if char.isdigit())
                    print("Сумма чисел в строке:", numbers_sum)

                elif choice == '3':
                    print(
                        "Введите ключи и значения для словаря (разделите ключ и значение пробелом, 'q' для завершения):")
                    user_dict = {}

                    while True:
                        user_input = input()
                        if user_input.lower() == 'q':
                            break

                        # Разделяем ввод на ключ и значение
                        input_parts = user_input.split()

                        if len(input_parts) != 2:
                            print("Некорректный ввод. Повторите попытку.")
                            continue

                        key, value = input_parts

                        if value.isdigit():
                            user_dict[key] = int(value)
                        else:
                            print("Некорректное значение. Введите целое число.")

                    keys_list = list(user_dict.keys())
                    print("Ключи словаря:", keys_list)

                    if user_dict:
                        min_value_key = min(user_dict, key=lambda k: user_dict[k])
                        print("Ключ с минимальным значением:", min_value_key)
                    else:
                        print("Словарь пустой.")

                elif choice == '4':

                    # Создать список из пользовательского ввода
                    print("Введите элементы списка через пробел:")
                    user_input = input()
                    user_list = [int(item) for item in user_input.split()]

                    unique_elements = list(set(user_list))
                    print("Уникальные элементы списка:", unique_elements)

                    if user_list:
                        min_val = min(user_list)
                        max_val = max(user_list)
                        min_index = user_list.index(min_val)
                        max_index = user_list.index(max_val)
                        user_list[min_index], user_list[max_index] = user_list[max_index], user_list[min_index]
                    print("Список с замененными минимальным и максимальным элементами:", user_list)
                else:
                    print("Некорректный выбор.")
                    process_input()
            process_input()
            pass

        elif choice == '3':
            rows = int(input('Введите количество строк: '))
            cols = int(input('Введите количество столбцов: '))

            matrix = []
            found_positive_row = None

            print('Введите элементы матрицы:')
            for i in range(rows):
                row = []
                for j in range(cols):
                    value = int(input(f'Введите элемент [{i}][{j}]: '))
                    row.append(value)

                if all(element > 0 for element in row) and found_positive_row is None:
                    found_positive_row = row

                matrix.append(row)
            print('Введенная матрица:')
            for row in matrix:
                print(row)

            if found_positive_row:
                sum_positive = sum(found_positive_row)
                print(f'Первая строка с положительными элементами: {found_positive_row}')
                print(f'Сумма положительных элементов: {sum_positive}')
            else:
                print('В матрице нет строк с положительными элементами.')

            pass

        elif choice == '4':
            def divide_numbers(a, b):
                try:
                    result = a / b
                    print("Результат деления:", result)
                except ZeroDivisionError:
                    print("Ошибка: деление на ноль!")
                finally:
                    print("Блок finally: завершение операции деления.")


            try:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
                divide_numbers(num1, num2)
            except ValueError:
                print("Ошибка: неверный формат числа.")
            pass
        elif choice == '5':
            print("Выход из программы")
            break
        else:
            print("Некорректный ввод, введите верное значение")

main_menu()
