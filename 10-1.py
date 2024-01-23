pets = {}

nickname = input("Введите кличку питомца: ")
vid = input("Введите вид питомца: ")
age = int(input("Введите возраст питомца: "))
name = input("Введите имя владельца: ")

pets[nickname] = {
     "Вид питомца": vid,
     "Возраст питомца": age,
     "Имя владельца": name
}

if age % 10 == 1 and age % 100 != 11:
    age_string = "год"
elif age % 10 in [2, 3, 4] and (age % 100 < 10 or age % 100 > 20):
    age_string = "года"
else:
    age_string = "лет"

info = f"Это {vid.lower()} по кличке \"{nickname}\". Возраст питомца: {age} {age_string}. Имя владельца: {name}"

print(info)