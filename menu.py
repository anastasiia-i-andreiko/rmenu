menu = []


def add_dish():
    name = input("Введіть назву: ")
    price = float(input("Введіть ціну: "))

    if price < 0:
        print("Ціна не може бути від'ємною")
        return

    desc = input("Введіть опис: ")
    category = input("Введіть категорію: ")

    dish = {
        "name": name,
        "price": price,
        "desc": desc,
        "category": category
    }

    menu.append(dish)
    print("Додано")


def show_menu():
    if len(menu) == 0:
        print("Меню пусте")
        return

    for i in range(len(menu)):
        print("-----")
        print("Назва:", menu[i]["name"])
        print("Ціна:", menu[i]["price"])
        print("Опис:", menu[i]["desc"])
        print("Категорія:", menu[i]["category"])
    print("-----")


def edit_dish():
    name = input("Введіть назву для редагування: ")
    found = False

    for i in range(len(menu)):
        if menu[i]["name"] == name:
            found = True
            menu[i]["price"] = float(input("Нова ціна: "))
            menu[i]["desc"] = input("Новий опис: ")
            menu[i]["category"] = input("Нова категорія: ")
            print("Змінено")

    if found == False:
        print("Не знайдено")


def delete_dish():
    print("1 - видалити по назві")
    print("2 - видалити по категорії")
    choice = input()

    if choice == "1":
        name = input("Назва: ")
        for i in range(len(menu)):
            if menu[i]["name"] == name:
                menu.pop(i)
                print("Видалено")
                break

    elif choice == "2":
        cat = input("Категорія: ")
        i = 0
        while i < len(menu):
            if menu[i]["category"] == cat:
                menu.pop(i)
            else:
                i = i + 1

        print("Видалено по категорії")

    print("Кількість страв:", len(menu))


def total_price():
    total = 0
    for i in range(len(menu)):
        total = total + menu[i]["price"]

    print("Загальна ціна:", total)


def price_by_category():
    cat = input("Введіть категорію: ")
    total = 0

    for i in range(len(menu)):
        if menu[i]["category"] == cat:
            total = total + menu[i]["price"]

    print("Сума:", total)


def sort_menu():
    print("1 - за зростанням")
    print("2 - за спаданням")
    choice = input()

    for i in range(len(menu)):
        for j in range(len(menu) - 1):
            if choice == "1":
                if menu[j]["price"] > menu[j + 1]["price"]:
                    temp = menu[j]
                    menu[j] = menu[j + 1]
                    menu[j + 1] = temp
            else:
                if menu[j]["price"] < menu[j + 1]["price"]:
                    temp = menu[j]
                    menu[j] = menu[j + 1]
                    menu[j + 1] = temp

    print("Відсортовано")


def main():
    while True:
        print("\n1 - додати")
        print("2 - показати")
        print("3 - редагувати")
        print("4 - видалити")
        print("5 - загальна ціна")
        print("6 - ціна по категорії")
        print("7 - сортування")
        print("0 - вихід")

        choice = input("Ваш вибір: ")

        if choice == "1":
            add_dish()
        elif choice == "2":
            show_menu()
        elif choice == "3":
            edit_dish()
        elif choice == "4":
            delete_dish()
        elif choice == "5":
            total_price()
        elif choice == "6":
            price_by_category()
        elif choice == "7":
            sort_menu()
        elif choice == "0":
            break
        else:
            print("Неправильно")


main()