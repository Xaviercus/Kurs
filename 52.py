def fibonacci(i):
    if i <= 0:
        return "blad"
    elif i == 1:
        return 0
    elif i == 2:
        return 1
    else:
        return fibonacci(i - 1) + fibonacci(i - 2)

print(fibonacci(20))

