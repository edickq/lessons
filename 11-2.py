pets = { }

def create():
    pet_name = input("Введите кличку питомца: ")
    pet_type = input("Введите вид питомца: ")
    pet_age = input("Введите возраст питомца: ")
    owner_name = input("Введите имя владельца: ")
    pets[pet_name] = {"вид": pet_type, "возраст": pet_age, "владелец": owner_name}
    print("Запись о питомце успешно создана!")

def read():
    pet_name = input("Введите кличку питомца, информацию о котором хотите посмотреть: ")
    if pet_name in pets:
        pet_info = pets[pet_name]
        print(f'Это {pet_info["вид"]} по кличке "{pet_name}". Возраст питомца: {pet_info["возраст"]} года. Имя владельца: {pet_info["владелец"]}')
    else:
        print("Питомец с такой кличкой не найден!")

def update():
    pet_name = input("Введите кличку питомца, информацию о котором хотите обновить: ")
    if pet_name in pets:
        pet_info = pets[pet_name]
        pet_type = input("Введите новый вид питомца: ")
        pet_age = input("Введите новый возраст питомца: ")
        owner_name = input("Введите новое имя владельца: ")
        pet_info["вид"] = pet_type
        pet_info["возраст"] = pet_age
        pet_info["владелец"] = owner_name
        print("Информация о питомце успешно обновлена!")
    else:
        print("Питомец с такой кличкой не найден!")

def delete():
    pet_name = input("Введите кличку питомца, информацию о котором хотите удалить: ")
    if pet_name in pets:
        del pets[pet_name]
        print("Запись о питомце успешно удалена!")
    else:
        print("Питомец с такой кличкой не найден!")

# Пример использования функций:
create()
read()
update()
delete()