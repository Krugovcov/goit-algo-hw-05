def caching_fibonacci():
    cache = {}
    def fibonacci(n):
        # Якщо n <= 0, повертаємо 0
        if n <= 0:
            return 0
        # Якщо n == 1, повертаємо 1
        elif n == 1:
            return 1
        # Якщо значення вже є у кеші, повертаємо його
        elif n in cache:
            return cache[n]
        # Інакше обчислюємо і зберігаємо у кеш
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci

# Отримуємо функцію fibonacci
fib = caching_fibonacci()

print(fib(10))
print(fib(15))
