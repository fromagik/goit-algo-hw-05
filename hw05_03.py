import os
import sys


def parse_log_line(line: str) -> dict:
    new_line = line.strip().split()
    date, time, log, disc = new_line[:1], new_line[1:2], new_line[2:3], new_line[3:]
    new_dict = {
        'Date' : " ".join(date),
        'Time' : " ".join(time),
        'Log' : ' '.join(log),
        'disc' : " ".join(disc)
    }
    return new_dict

def load_logs(file_path: str) -> list:
    lin = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                parse_log_line(line)
                line = line.strip()
                lin.append(line)

    return lin

def filter_logs_by_level(logs: list, level: str) -> list:
    print(f"Деталі логів для рівня '{level}':")
    for log in logs:
        if level in log:
            print(log)


def count_logs_by_level(logs: list) -> dict:
    pass


def display_log_counts(counts: dict):
    pass


if __name__ == '__main__':
    if len(sys.argv) > 1:
        path = sys.argv[1]
        level = sys.argv[2]
        filter_logs_by_level(load_logs(path), level)
    else: 
        path = os.getcwd()