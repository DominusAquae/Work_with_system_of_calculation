from class_int_n_system_calculation import int_n_system_calculation as new_int

# Вариант решения задачи уравнивания длины нескольких чисел, более оптимальный

a = new_int("111", 10)
b = new_int("111", 10)

print(f'{a, b} a == b :{a == b}, a != b : {a != b}, a > b : {a > b}, a >= b : {a >= b}, a <= b : {a <= b}, a < b : {a < b}')

a = new_int("111", 2)
b = new_int("111", 10)

print(f'{a, b} a == b :{a == b}, a != b : {a != b}, a > b : {a > b}, a >= b : {a >= b}, a <= b : {a <= b}, a < b : {a < b}')

a = new_int("100", 2)
b = new_int("111", 2)
print(f'{a, b} a == b :{a == b}, a != b : {a != b}, a > b : {a > b}, a >= b : {a >= b}, a <= b : {a <= b}, a < b : {a < b}')

a = new_int("0", 10)
b = new_int("100", 10)

print(f'{a, b} a == b :{a == b}, a != b : {a != b}, a > b : {a > b}, a >= b : {a >= b}, a <= b : {a <= b}, a < b : {a < b}')

a = new_int("0", 10)
b = new_int("0", 10)

print(f'{a, b} a == b :{a == b}, a != b : {a != b}, a > b : {a > b}, a >= b : {a >= b}, a <= b : {a <= b}, a < b : {a < b}')

a = new_int("111", 10)
b = new_int("0", 10)

print(f'{a, b} a == b :{a == b}, a != b : {a != b}, a > b : {a > b}, a >= b : {a >= b}, a <= b : {a <= b}, a < b : {a < b}')