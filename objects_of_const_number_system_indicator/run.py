from class_int_n_system_calculation import int_n_system_calculation as new_int

# Вариант решения задачи уравнивания длины нескольких чисел, более оптимальный
def max_len_arr (arr):
    return len(max(arr, key=len, default=0)) 

print(repr(new_int("10", 2)))
print(repr(new_int("120", 3)))
print(repr(new_int("0", 16)))