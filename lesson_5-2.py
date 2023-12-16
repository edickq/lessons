гласные = 0
согласные = 0
a = 0
e = 0
i = 0
o = 0
u = 0
y = 0
word = input("Введите слово: ")


for letter in word:
    if letter in ['a', 'e', 'i', 'o', 'u', 'y']:
        гласные += 1
        if letter == 'a':
            a += 1
        elif letter == 'e':
            e += 1
        elif letter == 'i':
            i += 1
        elif letter == 'o':
            o += 1
        elif letter == 'u':
            u += 1
        elif letter == 'y':
            y += 1
    else:
        согласные += 1

print("Количество гласных:", гласные)
print("Количество согласных:", согласные)
if a == 0:
    print("Количество 'a':False")
else:
    print("Количество 'a':", a)


if e == 0:
    print("Количество 'e':False")
else:
    print("Количество 'e':", e)

if i == 0:
    print("Количество 'i':False")
else:
    print("Количество 'i':", i)
if o == 0:
    print("Количество 'o':False")
else:
    print("Количество 'o':", o)
if u == 0:
    print("Количество 'u':False")
else:
    print("Количество 'u':", u)
if y == 0:
    print("Количество 'y':False")
else:
    print("Количество 'y':", y)





