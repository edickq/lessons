A = 200 # У Майкла
B = 200 # у Ивана 
X = 150 # минимальная сумма инвестиций

if A >= X and B >= X:
    print(2)   # Оба могут вложиться
elif A >= X:
    print("Mike")  # Только Майкл может вложиться
elif B >= X:
    print("Ivan")  # Только Иван может вложиться
elif A + B >= X:
    print(1)  # Вместе им хватает
else:
    print(0)  # Никто не может вложиться
