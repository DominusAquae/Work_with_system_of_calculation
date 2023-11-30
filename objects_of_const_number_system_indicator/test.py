from class_int_n_system_calculation import int_n_system_calculation
from class_int_n_system_calculation import N_numbers_to_equal_length
from class_int_n_system_calculation import sum_of_list_n_system_calculation

arr_add = []
arr_sub = []
arr_mul = []
for x in range(1000):
    for y in range(1000):
        a = int_n_system_calculation(str(x), 10)
        b = int_n_system_calculation(str(y), 10)
        '''
        if int(str(a + b)) != x + y:
            arr_add.append((x, y))
        '''
        if int(str(a - b)) != abs(x - y):
            arr_sub.append((x, y))
'''
        if int(str(a * b)) != x*y:
            arr_mul.append((x, y))
'''
print(arr_add)
print(arr_sub)
print(arr_mul)