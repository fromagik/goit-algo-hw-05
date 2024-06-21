from typing import Callable, Generator


def counter(string: str) -> Generator[float, None, None]:
    for num in string.split():
        try:
            yield float(num)
        except ValueError:
            continue

def sum_profit(text: str, func: Callable[[float], float]) -> float:
    return sum(list(counter(text))) 

s = 'Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів.'

total = sum_profit(s, counter)
print(f'Загальний дохід: {total}')
