from functools import lru_cache # Імортуємо модуль для роботи з кешем


@lru_cache(maxsize=256) # В декоратор передаємо значення 256, за замовчуванням 128
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        #Якшо значення береться не з кешу то виводитеметься строка яка підкреслюватиме роботу самої функції. 
        #Якщо вевидення число фібоначі буде без строки, це буде означати що результат взявся з кешу
        print(f'Count fibonnaci for {n} egal {str(result)}')
        return result # Повертаємо результат роботи функцій