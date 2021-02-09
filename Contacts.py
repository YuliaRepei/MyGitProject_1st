from exit_module import menu_exit
def main_menu():
    print("Главное меню (0)")
    print("Создать контакт (1)")
    print("Найти контакт (2)")
    print("Отредактировать контакт (3)")
    print("Удалить контакт (4)")
    print("Выйти (5)")
    command = input ("Пожалуйста, выберите действие: ")
    if command == "0":
        main_menu()
    elif command == "1":
        create_contact()
    elif command == "2":
        print ("К сожалению, функция недоступна")
    elif command == "3":
        print ("К сожалению, функция недоступна")
    elif command == "4":
        print ("К сожалению, функция недоступна")
    elif command == "5":
        menu_exit()
def create_contact():
    phone = input("Пожалуйста, введите номер телефона: ")
    name = input("Пожалуйста, введите имя: ")
    contacts[phone] = name
    print("Контакт был успешно добален")
    main_menu()
contacts = dict ()
main_menu()



