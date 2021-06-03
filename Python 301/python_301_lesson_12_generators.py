def my_generator():
    for num in range(50):
        yield num ** num

my_var_gen = my_generator()
all_numbers = list(my_var_gen)
print(all_numbers)

for big_num in my_generator():
    print(big_num)
