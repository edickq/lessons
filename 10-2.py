number = 10 
dict = {}
while number >= -5:
    print(f'number = {number} stepen = {number**number}')
    dict[number] = number**number 
    number -= 1
print(dict)