from data_base_bot import * # Імпортуємо модулі
from wrapper import *
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


@input_error
def add_contact(args): # Функція для добавлення контактів 
    if len(args) == 1:
        raise ValueError 
    elif len(args) > 2:
        raise IndexError 
    else:
        name, numer = args 
        set_contact(name, numer) # Виклик імпортованої функції з бази данний
        print("Contact added.")


@input_error
def change_contact(args): # Зміна номеру для контакта
    if len(args) == 1:
        raise ValueError
    elif len(args) > 2:
        raise IndexError
    elif is_table_empty():
        raise TypeError
    else:
        name, number = args 
        update_contact(name, number) # Виклик функції з бази данних
        print('Contact updated')


@input_error
def get_phone(args): # Функція для повернення номеру телефону 
    if len(args) != 1:
        raise IndexError
    else: 
        name = args[0] # Імя контакта як перший елемент  
        for number in numer_contact(name): # Цикл з функції що була імпортована з БД
            print(number)


@input_error
def get_all_contact(): # Повернення всіх контактів 
    if not is_table_empty():
        list_contacts = [] # Порожній список для всіх контактів
        for contact in get_contact(): # Ітерація з функції з БД
            dict_contact = {
                "Name"  : contact[0],
                'Number' : contact[1]
            } # Напомнюємо словник для кожного контакта
            list_contacts.append(dict_contact) # Наповнюємо список контактів та повертаємо його
        return list_contacts
    else: 
        raise TypeError


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