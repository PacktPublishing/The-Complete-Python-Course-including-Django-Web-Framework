def add_numbers(*args):
    total = 0
    for num in args:
        total = total + num
    return total

total = add_numbers(1, 3, 5, 7, 9)
print(total)
