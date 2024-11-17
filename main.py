# Самостоятельная работа по уроку "Рекурсия"

# def summa(n):
#     if n == 0:
#         return 0
#     else:
#         return n + summa(n -1)
#
# print(summa(123))

# stack = []
# stack.append(1)
# print("Добавили элемент" , stack)
# stack.append(2)
# print("Добавили элемент" , stack)
# stack.append(3)
# print("Добавили элемент" , stack)
# stack.append(4)
# print("Добавили элемент" , stack)
# print(stack)
# stack.pop()
# print("Убрали элемент" , stack)
# stack.pop()
# print("Убрали элемент" , stack)
# stack.pop()
# print("Убрали элемент" , stack)
# stack.pop()
# print("Убрали элемент" , stack)

def get_multiplied_digits(number):
    # Преобразуем число в строку
    str_number = str(number)

    # Если длина строки больше 1, продолжаем рекурсию
    if len(str_number) > 1:
        # Берем первую цифру
        first = int(str_number[0])
        # Умножаем первую цифру на результат рекурсивного вызова
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        # Если длина строки 1, возвращаем единственную цифру
        return int(str_number)

# Пример использования
result = get_multiplied_digits(40203)
print(result)  # Вывод: 24