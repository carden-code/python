# Подгруженные файлы (Классы)(модули)
from railway import Railway


NEWLINE = "\n" * 2

# Создаёт экземпляр класса Railway и выводит приветственное сообщение.
railway = Railway()

print(NEWLINE)
print("Добро пожаловать в программу 'Железная дорога'")
print(NEWLINE)

# Запуск меню (Цикл). С запросом ввода нужного пользователю пункта
# и передаёт результат в виде параметра методу selected.
while True:
    print(f"stations: {railway.stations}\n\n")
    print(f"trains: {railway.trains}\n\n")
    print(f"wagons: {railway.wagons}\n\n")
    print(f"routes: {railway.routes}\n\n")
    print(NEWLINE)
    railway.main_menu_items()
    item = input()
    if item == '0':
        break
    while True:
        if item == '1':
            railway.create_menu_items()
            menu_item = input()
            if menu_item == '0':
                break
            else:
                railway.selected(menu_item, item)
        elif item == '2':
            railway.perform_actions_objects_menu()
            menu_item = input()
            if menu_item == '0':
                break
            else:
                railway.selected(menu_item, item)
        elif item == '3':
            railway.view_information_objects_menu()
            menu_item = input()
            if menu_item == '0':
                break
            else:
                railway.selected(menu_item, item)

