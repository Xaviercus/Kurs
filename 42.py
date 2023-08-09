def silnia(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia(n - 1)


print("Silnia 5:", silnia(4))
