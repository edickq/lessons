import math
# количество рыбаков
количество_рыбаков = 3
# сколько кг может выдержать лодка
m = 150
# лодка помещает не более 2-х человек
max_n = 2
все_веса = []
# вводится вес каждого рыбака
for каждый_рыбак in range(количество_рыбаков):
    вес = int(input('вводи вес рыбака : '))
    все_веса.append(вес)
#Посчитать общий вес путем сложения всех_весов
общий_вес = sum(все_веса)
print(f'общий вес {общий_вес} кг')
# сколько лодок нужно
lodok_nugno = общий_вес/m
lodok_nugno = math.ceil(lodok_nugno)
print(f'лодок нужно {lodok_nugno} шт')