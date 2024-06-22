import os
from pathlib import Path

def parse_log_line(line: str) -> dict:
    new_line = line.split()
    date, time, log, disc = new_line[:1], new_line[1:2], new_line[2:3], new_line[3:]
    new_dict = {
        'Date' : " ".join(date),
        'Time' : " ".join(time),
        'Log' : ' '.join(log),
        'disc' : " ".join(disc)
    }

    return new_dict


def load_logs(file_path: str) -> list:
    # if os.path.exists(file_path):
    if file_path.is_file():
        with file_path.open('r') as file:
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
    pass


if __name__ == '__main__':
    # if len(sys.argv) > 1:
    #     try:
    #         path = sys.argv[1]
    #         level = sys.argv[2]
    #     except IndexError:
    #         path = sys.argv[1]
    path = Path('logs.txt')        
    #print(load_logs(path))
    # for parse in load_logs(path):
    #     print(parse_log_line(parse.strip()))
