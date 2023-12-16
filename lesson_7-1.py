N = int(input('Сколько чисел будет в списке? : '))  # вводим число N

nums = []  # создаем пустой список

# добавляем числа из ввода в перевернутом порядке
for all_items in range(N):
    num = int(input(f'вводи теперь свои числа {N} раз: '))
    nums.append(num)

# переворачиваем список
reversed_nums = nums[::-1]

# выводим перевернутый список
for num in reversed_nums:
    print(num)