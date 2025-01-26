
def evaluate_logical_expressions():

    x = float(input("Введите значение x: "))
    y = float(input("Введите значение y: "))

    result_a = (x**2 + y**2 <= 4) and (x == 1) and (y == -1)
    print(f"\nа) x^2 + y^2 ≤ 4 при x={x}, y={y}\n     Результат а: {result_a}\n")

    result_b = (x >= 0) or (y**2 != 4) and (x == 1) and (y == 2)
    print(f"б) (x ≥ 0) или (y^2 ≠ 4) при x={x}, y={y}\n     Результат б: {result_b}\n")


    result_c = (x >= 0) and (y**2 != 4) and (x == 1) and (y == 2)
    print(f"в) (x ≥ 0) и (y^2 ≠ 4) при x={x}, y={y}\n     Результат в: {result_c}\n")

    result_d = (x * y != 0) and (y > x) and (x == 2) and (y == 1)
    print(f"г) (x * y ≠ 0) и (y > x) при x={x}, y={y}\n     Результат г: {result_d}\n")

    result_e = (x * y != 0) or (y < x) and (x == 2) and (y == 1)
    print(f"д) (x * y ≠ 0) или (y < x) при x={x}, y={y}\n     Результат д: {result_e}\n")

    result_f = (not (x * y < 0)) and (y > x) and (x == 2) and (y == 1)
    print(f"е) (не (x * y < 0)) и (y > x) при x={x}, y={y}\n      Результат е: {result_f}\n")

    result_g = (not (x * y < 0)) or (y > x) and (x == 1) and (y == 2)
    print(f"ж) (не (x * y < 0)) или (y > x) при x={x}, y={y}\nРезультат ж: {result_g}\n")

evaluate_logical_expressions()
