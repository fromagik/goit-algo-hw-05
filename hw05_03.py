# for line in lst:
#     list_line = line.split(' ')
#     if list_line[2] == "INFO":
#         print(list_line[0] + ' ' + list_line[1] + ' - ' + " ".join(list_line[3:]))
from pathlib import Path

def parse_log_line(line: str) -> dict:
    new_line = line.strip().split()
    date, log, disc = new_line[:2], new_line[2:3], new_line[3:]
    new_dict = {
        'Date' : date,
        'Log' : log,
        'disc' : disc
    }
    return new_dict

def load_logs(file_path: str) -> list:
    lin = []
    if file_path.is_file():
        with file_path.open('r') as file:
            lines = file.readlines()
            for line in lines:
                parse_log_line(line)


file_path = Path('logs.txt')
load_logs(file_path)

def filter_logs_by_level(logs: list, level: str) -> list:
    pass


def count_logs_by_level(logs: list) -> dict:
    pass


def display_log_counts(counts: dict):
    pass

