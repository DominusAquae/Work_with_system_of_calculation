from class_int_n_system_calculation import int_n_system_calculation as new_int

# Вариант решения задачи уравнивания длины нескольких чисел, более оптимальный
def max_len_arr (arr):
    return len(max(arr, key=len, default=0)) 
arr = [new_int("10", 10), new_int("11", 10)]
print(new_int.N_numbers_to_equal_length(arr))

arr = [new_int("10", 2), new_int("1", 30)]
print(new_int.N_numbers_to_equal_length(arr))

arr = [new_int("10000", 3), new_int("11890888888", 10)]
print(new_int.N_numbers_to_equal_length(arr))