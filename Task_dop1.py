# Пользователь вводит целое число. Выведите его строку-описание вида
# "отрицательное четное число",
# "нулевое число", "положительное нечетное число", например,
# численным описанием числа 190 является строка "положительное четное число".

n = int(input("Введите число: "))
# if n < 0 and n %2==0: print("Отрицательное четное")
# elif n < 0 and n %2!=0: print("Отрицательное нечетное")
# elif n > 0 and n %2==0: print("Полодительное четное")
# elif n > 0 and n %2!=0: print("Положительное нечетное")
# else: print("Нулевое число")

# Второе решение
if n < 0:
    if n % 2 == 0:
        print("Отрицательное четное")
    else:
        print("Отрицательное нечетное")
elif n > 0:
    if n % 2 == 0:
        print("Полодительное четное")
    else:
        print("Положительное нечетное")
else:
    print("Нулевое число")
