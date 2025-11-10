from class_int_n_system_calculation import int_n_system_calculation as new_int

# Вариант решения задачи уравнивания длины нескольких чисел, более оптимальный
def max_len_arr (arr):
    return len(max(arr, key=len, default=0)) 

def f (a, b):
    return a + b

print(f(new_int("9", 10), new_int("9", 10)))