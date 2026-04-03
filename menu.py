menu = []

def add_dish():
    name = input("Введіть назву: ")
    price = float(input("Введіть ціну: "))
    if price < 0:
        print("Ціна не може бути від’ємною")
        return
    desc = input("Опишіть: ")
    dish = {"name": name, "price": price, "desc": desc}
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
    print("-----")

def main():
    while True:
        print("\n1 - додати")
        print("2 - показати")
        print("0 - вихід")
        choice = input("Ваш вибір: ")
        if choice == "1":
            add_dish()
        elif choice == "2":
            show_menu()
        elif choice == "0":
            break
        else:
            print("Неправильно")

main()