# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: 
# 7 
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 
# Вывод:
# 3 3 2 12      (каждое число вводится с новой строки)


n = int(input("Введите количество элементов первого массива N = "))
arrn = []
for i in range(n):
    arrn.append(int(input()))
print (arrn)

m = int(input("Введите количество элементов второго массива M = "))
arrm = []
for j in range(m):
    arrm.append(int(input()))
print(arrm)

def func(arrn, arrm):
    arr = []
    for i in range(len(arrm)):
        for j in range(len(arrn)):
            if arrm[i] != arrn[j]:
                arr.append(arrn[j])
    return arr

print(func(arrn, arrm)) 
