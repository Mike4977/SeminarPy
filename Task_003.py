# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

# import math
cab1 = int(input("Первый класс: "))
cab2 = int(input("Второй класс: "))
cab3 = int(input("Третий класс: "))

# print(math.ceil(cab1 / 2 + cab2 / 2 + cab3 / 2))

# Второе решение
# print(cab1 // 2  + cab2 // 2 + cab3 // 2 + cab1 % 2  + cab2 % 2 + cab3 % 2)

# третье решение

print((cab1 + 1) // 2 + (cab2 + 1) // 2 + (cab3 + 1) // 2)
