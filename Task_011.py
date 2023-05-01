# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

n = int(input("Введите число: "))
fib1 = 0
fib2 = 1
i = 2

while True:
    fib = fib1 + fib2
    if fib > n:
        break
    fib2 = fib1
    fib1 = fib
    if fib == n:
        print(i)
        break
    i+=1
if n != fib:
    print("-1")
    

# i = 2    
# for i in range(2, n):
#     fib = fib1 + fib2
#     if fib > n:
#         break
#     print(fib)
#     fib2 = fib1
#     fib1 = fib
#     i +=1
# if fib == n:
#     print(i)
# else: print("-1")

