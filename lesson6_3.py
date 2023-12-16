A = int(input('введите число номер 1 : '))
B = int(input('введите число номер 2 : '))
print('the line ')
for i in range(A, B+1):
    if i % 2 == 0:
        print(i, end=' ')