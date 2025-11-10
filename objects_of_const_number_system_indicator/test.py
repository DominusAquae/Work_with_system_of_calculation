from class_int_n_system_calculation import int_n_system_calculation

arr_add = []
arr_sub = []
arr_mul = []

for n in range(2, 11):
    print(n)
    for x in range(0, 100000):
        str_x = str(x)
        if any(elem in str_x for elem in "0123456789"[n:]):
            continue
        for y in range(0, 100000):
            str_y = str(y)
            if any(elem in str_y for elem in "0123456789"[n:]):
                continue
            a = int_n_system_calculation(str_x, n)
            b = int_n_system_calculation(str_y, n)
            
            if int(str(a + b), n) != int(str_x, n) + int(str_y, n):
                arr_add.append((x, y, n))
            
            # if int(str(a - b)) != abs(x - y):
            #     arr_sub.append((x, y))

            # if int(str(a * b)) != x*y:
            #     arr_mul.append((x, y))

    print(arr_add)
    print(arr_sub)
    print(arr_mul)