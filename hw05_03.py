import os
from pathlib import Path
import sys

def main():
    path = None
    level = None
    if len(sys.argv) > 1:
        try:
            path = sys.argv[1]
            level = sys.argv[2]
        except IndexError:
            path = sys.argv[1]
    
    if level:
        display_log_counts(count_logs_by_level(load_logs(path)))
        print(filter_logs_by_level(load_logs(path) ,level)[0])
        for logs in filter_logs_by_level(load_logs(path) ,level)[1]:
            print(logs)
    else:
        display_log_counts(count_logs_by_level(load_logs(path)))









def parse_log_line(line: str) -> dict:
    new_line = line.split()
    date, time, log, desc = new_line[:1], new_line[1:2], new_line[2:3], new_line[3:]
    new_dict = {
        'Date' : " ".join(date),
        'Time' : " ".join(time),
        'Log' : ' '.join(log),
        'Description' : " ".join(desc)
    }

    return new_dict


def load_logs(file_path: str) -> list:
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return [line.strip() for line in lines]


def filter_logs_by_level(logs: list, level: str) -> list:
    return [f"Деталі логів для рівня '{level}':", [log for log in logs if level in log]]
            


def count_logs_by_level(logs: list) -> dict:
    dictt = {
        'INFO' : 0,
        'DEBUG' : 0,
        'ERROR' : 0,
        'WARNING' : 0
    }
    for log in logs:
        log = log.strip().split()
        loge = " ".join(log[2:3])
        if loge in ['INFO','DEBUG','ERROR','WARNING']:
            dictt[loge] += 1
    return dictt


def display_log_counts(counts: dict):
    level_logs = 'Рівень логування'
    quantity_logs = 'Кількість'
    first_line = f"{level_logs:^10}|{quantity_logs:^10}"
    print(first_line)
    print('-'*len(level_logs) + '|' + '-' * len(quantity_logs))
    for key, value in counts.items():
        print(f'{key:^16}|{value:^10}')


if __name__ == '__main__':
    main()