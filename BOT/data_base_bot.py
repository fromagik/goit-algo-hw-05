import sqlite3

#Create connection
def get_connection(): # Конектимо базу данних 
    return sqlite3.connect('bot_data_base.db')


#Cтворюємо таблицю 
def create_table():
    connect = get_connection() # підключення до бази данних 
    cursor = connect.cursor() # Курсор для створення запитів 
    cursor.execute(''' CREATE TABLE IF NOT EXISTS contacts (
                   name TEXT NOT NULL,
                   number TEXT UNIQUE) ''') # Виконання запиту БД
    connect.commit() # Збереження змін
    connect.close() # Закриваємо підключення

def set_contact(name, number): # Додаємо контакт
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute('INSERT INTO contacts(name, number) VALUES (?, ?)', (name, number))
    connect.commit()
    connect.close()

def get_contact(): # Отримуємо список всіх контактів
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM contacts')
    contacts = cursor.fetchall()
    connect.commit()
    connect.close()
    return contacts # Повернення списку всіх контакта

def update_contact(name, number): # Зміна номеру для контакта
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute('UPDATE contacts SET number = ? WHERE name = ?', (number, name))
    connect.commit()
    connect.close()


def numer_contact(name): # Повернення номеру телефона для контакта
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute('SELECT number FROM contacts WHERE name = ?', (name, ))
    contact_numer = cursor.fetchone()
    connect.commit()
    connect.close()
    return contact_numer 

def table_exist(table_name): # Перевірка на існування таблиці
    connect = get_connection()
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM sqlite_master WHERE type = 'table' AND name = ?", (table_name, ))
    exists = cursor.fetchone() is not None 
    connect.close()
    return exists

def is_table_empty(): # Добавив перевірку на заповнення таблиці 
    connect = sqlite3.connect()
    cursor = connect.cursor()
    cursor.execute(f"SELECT COUNT(*) FROM contacts;")
    count = cursor.fetchone()[0]
    connect.close()
    return count == 0 # Повертає True якщо таблиця пуста і False якщо заповнена
