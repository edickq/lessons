import math

X = int(input("Введите число X: "))

count = 0

for i in range(1, int(math.sqrt(X)) + 1):
    if X % i == 0:
        count += 1

count += 2

print("Количество натуральных делителей числа X:", count)