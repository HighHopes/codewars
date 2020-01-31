def is_very_even_number(n):
    if n == 0:
        return True
    if n % 9 == 0:
        return 9
    else:
        return n % 9

print(is_very_even_number(87))
