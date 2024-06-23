import os
import sys

def main():
    """
    Основна функція що не приймає аргументів, та служить для обьеднання всіх функцій та проведення маніпуляцій над ними в одному місці
    """
    if len(sys.argv) < 2:
        print("Помилка: Не вказано шлях до файлу.")
        sys.exit(1)
    """
    Перший аргумент з індексом 0 це назва файлу що виконується, 
    з індексом 1 це шлях до файлу з логами що присвоюється перемінній path, 
    з індексом 2 це рівень логування який вказується при запуску програми та присвоюється перемінній level 
    """
    path = sys.argv[1] 
    level = sys.argv[2] if len(sys.argv) > 2 else None
    
    if path:
        logs = load_logs(path)
        if not logs:
            sys.exit(1)
        
        if level:
            display_log_counts(count_logs_by_level(logs))
            print(f"Деталі логів для рівня '{level.upper()}':")
            for log in filter_logs_by_level(logs, level):
                print(log)
        else:
            display_log_counts(count_logs_by_level(logs))


def load_logs(file_path: str) -> list:
    """
    Функція приймає шлах до файлу як аргумент та повертає список кожного рядка логування 
    """
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                return [line.strip() for line in file]
        else:
            print(f"Помилка: файл '{file_path}' не знайдено.")
            return []
    except IOError:
        print(f"Помилка: файл '{file_path}' неможливо відкрити")
        return []
    

def parse_log_line(line: str) -> dict:
    """
    функція приймає рядок логування та повертає словник з датою, часом, назвою логу та описом
    """
    new_line = line.split()
    date, time, log, desc = new_line[0], new_line[1], new_line[2]
    desc = " ".join(new_line[3:]) # Опис рядку логування це зріз списку починаючи з індекса 3 і до кінця
    new_dict = {
        'Date' : date,
        'Time' : time,
        'Log' : log,
        'Description' : desc
    }

    return new_dict


def filter_logs_by_level(logs: list, level: str) -> list:
    """
    функція фільтрує логування по рівнях та повертає список для кожного рівня логування
    """
    return [log for log in logs if level.upper() in log]
            

def count_logs_by_level(logs: list) -> dict:
    # Функція підраховує кількість логувань за рівнями 
    levels = ['INFO', 'DEBUG', 'ERROR', 'WARNING']
    """
    Функція повертає словник з ключем як назва логу 
    та кількість логів. 
    Для підрахунку логу я використав:
        функцію filter з лямбда-функцією що повертає логування якщо воно знаходиться на тому самому рівні
        перетворив це все в список що заповнений позитивними булевими виразами для кожного логу що знаходиться на заданому рівні
        та повернув його довжину функцією len що поверне число яке й буде кількістью кожного логу в файлі 
    """
    return {level: len(list(filter(lambda log: level in log, logs))) for level in levels} 


def display_log_counts(counts: dict):
    """
    Функція що приймає попередню функцію як агрумент та виводить назву та кількість логів в зручному форматі 
    """
    level_logs = 'Рівень логування'
    quantity_logs = 'Кількість'
    first_line = f"{level_logs:^18}|{quantity_logs:^12}"
    print(first_line)
    print('-' * 18 + '|' + '-' * 12)
    for key, value in counts.items():
        print(f'{key:^18}|{value:^10}')


if __name__ == '__main__':
    main()