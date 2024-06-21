from data_base_HW04 import * # Імпортуємо модулі
import time


def main(): # Основна функція
    
    if not table_exist('contacts'): # Створюємо базу данних якщо її не існує
        create_table()

    print("Welcome to the assistant bot!")
    time.sleep(2)
    print("How can I help you?")
    while True: # Основний цикл
        user_command = input('Enter you command (help to display all commands): ')
        cmd, *args = parse_input(user_command)
        if len(args) >= 3:
            print('We are problme, need max 2 arguments')
        if cmd in ['exit', 'close']:
            print('Goodbay!!!')
            break
        elif cmd == 'add': # Додавання контакту
            add_contact(args)
        elif cmd == 'change': # Зміна номеру для контакта
            change_contact(args)
        elif cmd == 'phone':
            get_phone(args) # Номер контакта
        elif cmd == 'all':
            print(get_all_contact())
        elif cmd == 'help': # Список можливих функцій
            help()
        else:
            print('Invalid command.')


def parse_input(user_input): # Парсинг введених команд користувачем
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args # Повертає команду як перший агрумент і список як решту аргументів 


def add_contact(args): # Функція для добавлення контактів 
    name, numer = args 
    set_contact(name, numer) # Виклик імпортованої функції з бази данний
    print("Contact added.")


def change_contact(args): # Зміна номеру для контакта
    name, number = args 
    update_contact(name, number) # Виклик функції з бази данних
    print('Contact updated')


def get_phone(args): # Функція для повернення номеру телефону 
    name = args[0] # Імя контакта як перший елемент  
    for number in numer_contact(name): # Цикл з функції що була імпортована з БД
        print(number)


def get_all_contact(): # Повернення всіх контактів 
    list_contacts = [] # Порожній список для всіх контактів
    for contact in get_contact(): # Ітерація з функції з БД
        dict_contact = {
            "Name"  : contact[0],
            'Number' : contact[1]
        } # Напомнюємо словник для кожного контакта
        list_contacts.append(dict_contact) # Наповнюємо список контактів та повертаємо його
    return list_contacts


def help(): # Меню допомоги
    print("'add' for add new contact")
    time.sleep(2)
    print("'change' for update contact")
    time.sleep(2)
    print("'phone' to get a number by contact name")
    time.sleep(2)
    print("'all' to get all contacts")
    time.sleep(2)    
    print('SYNTAXIS COMMANDS: <command> <name_contact> <number>')

if __name__ == '__main__': #Виклик основної функції якщо імя файлу основне 
    main()